import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
def test_url_status(base_url, code, request_method):
    target = f"{base_url}/status/{code}"
    response = request_method(url=target)
    assert response.status_code == code, f"Got unexpected code: {code}"
