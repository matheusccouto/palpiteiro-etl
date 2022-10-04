"""Unit tests for the lambda function."""

from fnmatch import fnmatch

import pytest

import odds_extract
import utils.aws.s3
import utils.test


def test_uri():
    """Test if lambda handler return the file URI."""
    results = odds_extract.handler(event={})
    assert fnmatch(results["uri"], "s3://palpiteiro-test/brasileirao/*-*-*T*:*:*.json")


@pytest.fixture(name="delete_odds")
def fixture_delete_odds():
    """Clear odds dir from palpiteiro-test."""
    yield
    utils.aws.s3.delete("s3://palpiteiro-test/brasileirao")


def test_is_serializable(delete_odds):  # pylint: disable=unused-argument
    """Test if return is serializable."""
    results = odds_extract.handler(event={})
    assert utils.test.is_serializable(results)


def test_exists(delete_odds):  # pylint: disable=unused-argument
    """Test if JSON file exists."""
    results = odds_extract.handler(event={})
    assert utils.aws.s3.exists(results["uri"])
