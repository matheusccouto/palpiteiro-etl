"""Create README.md overview diagram."""

# pylint: disable=expression-not-assigned

import os

from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.gcp.analytics import Bigquery

THIS_DIR = os.path.dirname(__file__)
ICONS_DIR = os.path.join(THIS_DIR, "icons")


with Diagram(
    filename=os.path.join(THIS_DIR, "overview"),
    show=False,
    curvestyle="curved",
    direction="TB"
):

    cartola = Custom("cartola", os.path.join(ICONS_DIR, "cartola.png"))
    fivethirtyeight = Custom("fivethirtyeight", os.path.join(ICONS_DIR, "538.png"))
    odds = Custom("the-odds-api", os.path.join(ICONS_DIR, "the_odds_api.png"))
    warehouse = Bigquery("big query")

    cartola >> StepFunctions("players") >> warehouse
    cartola >> StepFunctions("scouts") >> warehouse
    cartola >> StepFunctions("matches") >> warehouse
    fivethirtyeight >> StepFunctions("spi") >> warehouse
    odds >> StepFunctions("odds") >> warehouse


with Diagram(
    "\nCartola Players",
    filename=os.path.join(THIS_DIR, "state-machine-cartola-players"),
    show=False,
    curvestyle="curved",
):
    with Cluster("state machine"):
        extract = Lambda("extract")
        json = S3("json")
        transform = Lambda("transform")
        csv = S3("csv")
        load = Lambda("load")
    (
        Custom("/atletas/mercado", os.path.join(ICONS_DIR, "cartola.png"))
        >> extract
        >> json
        >> transform
        >> csv
        >> load
        >> Bigquery("cartola\natletas")
    )


with Diagram(
    "\nCartola Scouts",
    filename=os.path.join(THIS_DIR, "state-machine-cartola-scouts"),
    show=False,
    curvestyle="curved",
):
    with Cluster("state machine"):
        extract = Lambda("extract")
        json = S3("json")
        transform = Lambda("transform")
        csv = S3("csv")
        load = Lambda("load")
    (
        Custom("/atletas/pontuados", os.path.join(ICONS_DIR, "cartola.png"))
        >> extract
        >> json
        >> transform
        >> csv
        >> load
        >> Bigquery("cartola\npontuados")
    )


with Diagram(
    "\nCartola Matches",
    filename=os.path.join(THIS_DIR, "state-machine-cartola-matches"),
    show=False,
    curvestyle="curved",
):
    with Cluster("state machine"):
        extract = Lambda("extract")
        json = S3("json")
        transform = Lambda("transform")
        csv = S3("csv")
        load = Lambda("load")
    (
        Custom("/partidas", os.path.join(ICONS_DIR, "cartola.png"))
        >> extract
        >> json
        >> transform
        >> csv
        >> load
        >> Bigquery("cartola\npartidas")
    )


with Diagram(
    "\nFiveThirtyEight SPI",
    filename=os.path.join(THIS_DIR, "state-machine-fivethirtyeight-spi"),
    show=False,
    curvestyle="curved",
):
    with Cluster("state machine"):
        extract = Lambda("extract")
        json = S3("json")
        transform = Lambda("transform")
        csv = S3("csv")
        load = Lambda("load")
    (
        Custom("/soccer-api/club", os.path.join(ICONS_DIR, "538.png"))
        >> extract
        >> json
        >> transform
        >> csv
        >> load
        >> Bigquery("fivethirtyeight\nspi")
    )


with Diagram(
    "\nOdds",
    filename=os.path.join(THIS_DIR, "state-machine-odds"),
    show=False,
    curvestyle="curved",
):
    with Cluster("state machine"):
        extract = Lambda("extract")
        json = S3("json")
        transform = Lambda("transform")
        csv = S3("csv")
        load = Lambda("load")
    (
        Custom("/soccer_brazil_campeonato", os.path.join(ICONS_DIR, "the_odds_api.png"))
        >> extract
        >> json
        >> transform
        >> csv
        >> load
        >> Bigquery("odds\nbrasileirao")
    )
