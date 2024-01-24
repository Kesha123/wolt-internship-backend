import json
import pytest
from tornado.httpclient import HTTPClientError


@pytest.mark.gen_test
def test_api(http_client, base_url, mock_payload):
    response = yield http_client.fetch(
            f"{base_url}/api/delivery-fee-calculator",
            method="POST",
            body=json.dumps(mock_payload)
        )
    assert response.body == b'{"delivery_fee": 710}'
    assert response.code == 200


@pytest.mark.gen_test
def test_api_bad_request(http_client, base_url, mock_bad_payload):
    for payload in mock_bad_payload:
        with pytest.raises(HTTPClientError) as exc_info:
            response = yield http_client.fetch(
                f"{base_url}/api/delivery-fee-calculator",
                method="POST",
                body=json.dumps(payload)
            )

        assert exc_info.value.code == 400

