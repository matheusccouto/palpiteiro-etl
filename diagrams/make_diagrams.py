"""Create README.md overview diagram."""

# pylint: disable=expression-not-assigned,pointless-statement

import os

from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.gcp.analytics import Bigquery

THIS_DIR = os.path.dirname(__file__)
ICONS_DIR = os.path.join(THIS_DIR, "icons")
CARTOLA_PATH = os.path.join(ICONS_DIR, "cartola.png")
FIVETHIRTYEIGHT_PATH = os.path.join(ICONS_DIR, "538.png")
ODDS_PATH = os.path.join(ICONS_DIR, "the_odds_api.png")


with Diagram(
    filename=os.path.join(THIS_DIR, "architecture"),
    show=False,
):

    # Warehouse

    bigquery = Bigquery("bigquery")

    # ETLs

    cartola_atletas_mercado = Custom("/atletas/mercado", CARTOLA_PATH)
    cartola_atletas_pontuados = Custom("/atletas/pontuados", CARTOLA_PATH)
    cartola_partidas = Custom("/partidas", CARTOLA_PATH)
    cartola_mercado_selecao = Custom("/mercado/selecao", CARTOLA_PATH)
    cartola_mercado_destaques = Custom("/mercado/destaques", CARTOLA_PATH)
    fivethirtyeight = Custom("/soccer-api/club", FIVETHIRTYEIGHT_PATH)
    odds = Custom("/soccer_brazil_campeonato", ODDS_PATH)
    load = Lambda("load")
    with Cluster("players"):
        (
            cartola_atletas_mercado
            >> Lambda("extract")
            >> S3("json")
            >> Lambda("transform")
            >> S3("csv")
            >> load
        )
    with Cluster("scouts"):
        (
            cartola_atletas_pontuados
            >> Lambda("extract")
            >> S3("json")
            >> Lambda("transform")
            >> S3("csv")
            >> load
        )
    with Cluster("matches"):
        (
            cartola_partidas
            >> Lambda("extract")
            >> S3("json")
            >> Lambda("transform")
            >> S3("csv")
            >> load
        )
    with Cluster("squad line up"):
        (
            cartola_mercado_selecao
            >> Lambda("extract")
            >> S3("json")
            >> Lambda("transform")
            >> S3("csv")
            >> load
        )
    with Cluster("popular line up"):
        (
            cartola_mercado_destaques
            >> Lambda("extract")
            >> S3("json")
            >> Lambda("transform")
            >> S3("csv")
            >> load
        )
    with Cluster("spi"):
        fivethirtyeight >> Lambda("extract") >> S3("csv") >> load
    with Cluster("odds"):
        (
            odds
            >> Lambda("extract")
            >> S3("json")
            >> Lambda("transform")
            >> S3("csv")
            >> load
        )
    load >> bigquery
