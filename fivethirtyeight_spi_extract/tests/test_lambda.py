"""Unit tests for the lambda function."""

from fnmatch import fnmatch

import pytest

import fivethirtyeight_spi_extract
import utils.aws.s3
import utils.test


def test_uri():
    """Test if lambda handler return the file URI."""
    results = fivethirtyeight_spi_extract.handler(event={})
    assert fnmatch(results["uri"], "s3://palpiteiro-test/spi/*-*-* *:*:*.csv")


@pytest.fixture(name="delete_spi")
def fixture_delete_atletas_mercado():
    """Clear atletas/mercado dir from palpiteiro-test."""
    yield
    utils.aws.s3.delete("s3://palpiteiro-test/spi")


def test_is_serializable(delete_spi):  # pylint: disable=unused-argument
    """Test if return is serializable."""
    results = fivethirtyeight_spi_extract.handler(event={})
    assert utils.test.is_serializable(results)


def test_exists(delete_spi):  # pylint: disable=unused-argument
    """Test if JSON file exists."""
    results = fivethirtyeight_spi_extract.handler(event={})
    assert utils.aws.s3.exists(results["uri"])
