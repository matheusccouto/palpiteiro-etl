"""Unit tests for the lambda function."""

import os
from fnmatch import fnmatch

import pytest

import odds_transform
import utils.aws.s3
import utils.test

THIS_DIR = os.path.dirname(__file__)


@pytest.fixture(name="setup_and_teardown")
def fixture_setup_and_teardown():
    """Setup and teardown palpiteiro-test."""
    with open(os.path.join(THIS_DIR, "sample.json"), encoding="utf-8") as file:
        utils.aws.s3.save(file.read(), "s3://palpiteiro-test/brasileirao/test.json")
    yield
    utils.aws.s3.delete("s3://palpiteiro-test/brasileirao")


def test_is_serializable(setup_and_teardown):  # pylint: disable=unused-argument
    """Test if return is serializable."""
    results = odds_transform.handler(
        event={"uri": "s3://palpiteiro-test/brasileirao/test.json"},
    )
    assert utils.test.is_serializable(results)


def test_uri(setup_and_teardown):  # pylint: disable=unused-argument
    """Test if lambda handler return the file URI."""
    results = odds_transform.handler(
        event={"uri": "s3://palpiteiro-test/brasileirao/test.json"},
    )
    assert fnmatch(results["uri"], "s3://palpiteiro-test/brasileirao/test.csv")


def test_exists(setup_and_teardown):  # pylint: disable=unused-argument
    """Test if CSV file exists."""
    results = odds_transform.handler(
        event={"uri": "s3://palpiteiro-test/brasileirao/test.json"}
    )
    assert utils.aws.s3.exists(results["uri"])
