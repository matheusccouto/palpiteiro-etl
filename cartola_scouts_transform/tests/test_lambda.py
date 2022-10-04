"""Unit tests for the lambda function."""

import os
from fnmatch import fnmatch

import pytest

import cartola_scouts_transform
import utils.aws.s3
import utils.test

THIS_DIR = os.path.dirname(__file__)


@pytest.fixture(name="setup_and_teardown")
def fixture_setup_and_teardown():
    """Setup and teardown palpiteiro-test."""
    with open(os.path.join(THIS_DIR, "sample.json"), encoding="utf-8") as file:
        utils.aws.s3.save(
            file.read(), "s3://palpiteiro-test/atletas/pontuados/2022-06.json"
        )
    yield
    utils.aws.s3.delete("s3://palpiteiro-test/atletas/pontuados")


def test_uri(setup_and_teardown):  # pylint: disable=unused-argument
    """Test if lambda handler return the file URI."""
    results = cartola_scouts_transform.handler(
        event={"uri": "s3://palpiteiro-test/atletas/pontuados/2022-06.json"},
    )
    assert fnmatch(results["uri"], "s3://palpiteiro-test/atletas/pontuados/2022-06.csv")


def test_is_serializable(setup_and_teardown):  # pylint: disable=unused-argument
    """Test if return is serializable."""
    results = cartola_scouts_transform.handler(
        event={"uri": "s3://palpiteiro-test/atletas/pontuados/2022-06.json"}
    )
    assert utils.test.is_serializable(results)


def test_exists(setup_and_teardown):  # pylint: disable=unused-argument
    """Test if CSV file exists."""
    results = cartola_scouts_transform.handler(
        event={"uri": "s3://palpiteiro-test/atletas/pontuados/2022-06.json"}
    )
    assert utils.aws.s3.exists(results["uri"])
