import pytest


def pytest_addoption(parser) -> None:
    parser.addoption("--url", 
                     default="dog.ceo",
                     help="Type base url. Example - 'dog.ceo'")


@pytest.fixture(scope='session')
def url(request) -> str:
    base_url = f"https://{request.config.getoption('url')}/api/"
    return base_url
