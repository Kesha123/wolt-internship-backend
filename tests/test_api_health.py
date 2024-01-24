import pytest


@pytest.mark.gen_test
def test_api_health(http_client, base_url):
    response = yield http_client.fetch(f"{base_url}/api/health_")
    assert response.code == 200