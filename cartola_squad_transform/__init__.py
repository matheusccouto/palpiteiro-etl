"""Transform most popular players data from Cartola FC."""

import json
import os

import pandas as pd

import utils.aws.s3
import utils.http

LINE_UPS = ["selecao", "capitaes", "reservas"]


def handler(event, context=None):  # pylint: disable=unused-argument
    """Lambda handler."""
    # Load
    data = json.loads(utils.aws.s3.load(event["uri"]))

    players = []
    for line_up in LINE_UPS:
        for player in data[line_up]:
            player.update(player.pop("Atleta"))
            player["selecao"] = line_up
            players.append(player)

    dataframe = pd.DataFrame.from_records(players)
    dataframe["temporada"] = data["temporada"]
    dataframe["rodada"] = data["rodada"]
    dataframe["ranking"] = (
        dataframe.groupby("selecao")["escalacoes"]
        .rank("first", ascending=False)
        .astype(int)
    )

    # Save as CSV
    uri = os.path.splitext(event["uri"])[0] + ".csv"
    utils.aws.s3.save(data=dataframe.to_csv(index=False), uri=uri)
    return {"uri": uri}
