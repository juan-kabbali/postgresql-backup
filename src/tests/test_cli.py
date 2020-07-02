import pytest

from src.pgbackup import cli

url = "postgres://user@example.com:5432/db_name"
driver_flag = "--driver"
driver_value = "local"
driver_unknown_value = "digital_ocean"
destination = "/some/backup/path"


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, driver_flag, driver_unknown_value, destination])


def test_parser_with_known_driver(parser):
    """
    The parser will not exit if the driver name is known
    """
    for driver in cli.known_drivers:
        assert parser.parse_args([url, driver_flag, driver, destination])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, driver_flag, driver_value])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and destination
    """
    args = parser.parse_args([url, driver_flag, driver_value, destination])
    assert args.url == url
    assert args.driver == driver_value
    assert args.destination == destination
