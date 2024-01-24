import pytest
from tornado.httpclient import HTTPClientError

@pytest.mark.gen_test
def test_api_health(http_client, base_url):
    response = yield http_client.fetch(f"{base_url}/api/health_")
    assert response.code == 200


@pytest.mark.gen_test
def test_api_not_existing_path(http_client, base_url):
    with pytest.raises(HTTPClientError) as exc_info:
        response = yield http_client.fetch(f"{base_url}/api/not-existing-path")
    assert exc_info.value.code == 404