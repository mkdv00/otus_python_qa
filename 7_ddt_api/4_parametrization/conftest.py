import pytest


@pytest.fixture(params=[4, 5, 6], ids=["Four", "Five", "Six"])
def param_fixture(request):
    return request.param


@pytest.fixture(scope='session')
def base_url():
    return "https://jsonplaceholder.typicode.com"
