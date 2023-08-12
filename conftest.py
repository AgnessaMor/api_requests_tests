import logging

import pytest

from fixtures.app import ClientApp

logger = logging.getLogger("api")

api_versions = {"api_v1": "/api/v1", "api_v2": "/api/v2"}
client_group_name = "UJET Reporting"


def pytest_addoption(parser):
    """Parser for comand-line params"""
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        help="my option: type1 or type2",
    )


@pytest.fixture(scope="session")
def app():
    url = "http://localhost:56733"
    logger.info(f"Start api tests, url is {url}")
    yield ClientApp(url)
