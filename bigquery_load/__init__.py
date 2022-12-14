"""Load CSV data into Bigquery."""

import io
import json
import os
import time
import random
import zoneinfo

import numpy as np
import pandas as pd
from google.cloud import bigquery


import utils.aws.s3
import utils.google

TZ = zoneinfo.ZoneInfo("UTC")
DTYPES = {
    "INTEGER": pd.Int64Dtype(),
    "FLOAT": "float64",
    "STRING": pd.StringDtype(),
    "BOOLEAN": pd.BooleanDtype(),
    "TIMESTAMP": pd.DatetimeTZDtype(tz=TZ),
}

creds = utils.google.get_creds_from_env_vars()
client = bigquery.Client(credentials=creds)


def run_query(query):
    """Run a query in BigQuery."""
    job = client.query(query)

    while not job.done():
        time.sleep(0.1)

    if job.errors:
        raise RuntimeError(json.dumps(job.errors))

    return job.num_dml_affected_rows


def random_number_string():
    """Random string formed only by numbers.."""
    return str(random.random())[2:]


def handler(event, context=None):  # pylint: disable=unused-argument
    """Lambda handler."""
    if event["table"] is None:
        event["table"] = os.path.splitext(os.path.basename(event["uri"]))[0]

    table = f"{creds.project_id}.{event['schema']}.{event['table']}"

    file = utils.aws.s3.load(event["uri"])
    data = pd.read_csv(io.StringIO(file))
    data["loaded_at"] = pd.Timestamp.now(tz=TZ)

    if event["type"] == "replace":
        data.convert_dtypes().to_gbq(
            destination_table=table,
            if_exists="replace",
            credentials=creds,
        )
        return {"statusCode": 200}

    tmp_table = f"{event['schema']}.tmp_{event['table']}{random_number_string()}"
    table_schema = {
        field.name: DTYPES[field.field_type]
        for field in client.get_table(table).schema
        if field.name in data.columns
    }
    data.astype(table_schema).to_gbq(
        destination_table=tmp_table,
        if_exists="replace",
        credentials=creds,
    )

    cols = ", ".join(data.columns)
    match = " AND ".join([f"a.{col} = b.{col}" for col in event["subset"]])
    update = ", ".join([f"a.{col} = b.{col}" for col in data.columns])

    num_dml_affected_rows = run_query(
        f"""
    MERGE `{table}` a
    USING `{tmp_table}` b
        ON {match}
    WHEN MATCHED THEN
        UPDATE SET {update}
    WHEN NOT MATCHED THEN
        INSERT ({cols}) VALUES ({cols})
    """
    )

    client.delete_table(tmp_table)
    return {
        "statusCode": 200,
        "num_affected_rows": num_dml_affected_rows,
    }
