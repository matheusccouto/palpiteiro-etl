"""Extract most popular line up players data from Cartola FC."""

import json
import os

import utils.aws.s3
import utils.http

SQUAD_URL = "https://api.cartola.globo.com/mercado/selecao"
STATUS_URL = "https://api.cartola.globo.com/mercado/status"


def handler(event, context=None):  # pylint: disable=unused-argument
    """Lambda handler."""
    status = utils.http.get(STATUS_URL)
    if status["game_over"]:
        raise ConnectionAbortedError("Extraction aborted. Game is over.")

    squad = utils.http.get(SQUAD_URL)

    # This endpoint returns has no reference at all for which season this is.
    # This is important to us as we work with multiseason data.
    # I'll include it inside the players that that are inside the 'atletas' key.

    season = status["temporada"]
    rnd = status["rodada_atual"]

    squad["temporada"] = season
    squad["rodada"] = rnd

    bucket = os.getenv("BUCKET_NAME")
    key = f"mercado/selecao/{season}-{rnd:02d}.json"
    uri = f"s3://{bucket}/{key}"
    utils.aws.s3.save(data=json.dumps(squad), uri=uri)
    return {"uri": uri}
