"""Unit tests for the lambda function."""

from fnmatch import fnmatch

import transfermarkt_extract
import utils.aws.s3
import utils.test


def test_is_serializable():
    """Test if return is serializable."""
    results = transfermarkt_extract.handler(event={})
    assert utils.test.is_serializable(results)


def test_uri():
    """Test if lambda handler return the file URI."""
    results = transfermarkt_extract.handler(event={})
    assert len(results) > 1
    assert fnmatch(results[0]["uri"], "s3://palpiteiro-test/*/*.csv")


def test_exists():  # pylint: disable=unused-argument
    """Test if file exists."""
    results = transfermarkt_extract.handler(event={})
    for row in results:
        assert utils.aws.s3.exists(row["uri"])
