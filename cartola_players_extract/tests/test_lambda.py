"""Unit tests for the lambda function."""

from fnmatch import fnmatch

import pytest

import cartola_players_extract
import utils.aws.s3
import utils.test


def test_uri():
    """Test if lambda handler return the file URI."""
    results = cartola_players_extract.handler(event={})
    assert fnmatch(results["uri"], "s3://palpiteiro-test/atletas/mercado/20*-*.json")


@pytest.fixture(name="delete_atletas_mercado")
def fixture_delete_atletas_mercado():
    """Clear atletas/mercado dir from palpiteiro-test."""
    yield
    utils.aws.s3.delete("s3://palpiteiro-test/atletas/mercado")


def test_is_serializable(delete_atletas_mercado):  # pylint: disable=unused-argument
    """Test if return is serializable."""
    results = cartola_players_extract.handler(event={})
    assert utils.test.is_serializable(results)


def test_exists(delete_atletas_mercado):  # pylint: disable=unused-argument
    """Test if JSON file exists."""
    results = cartola_players_extract.handler(event={})
    assert utils.aws.s3.exists(results["uri"])
