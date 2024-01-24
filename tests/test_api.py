import json
import pytest


@pytest.mark.gen_test
def test_api_health(http_client, base_url, mock_payload):
    response = yield http_client.fetch(
            f"{base_url}/api/delivery-fee-calculator",
            method="POST",
            body=json.dumps(mock_payload)
        )
    assert response.body == b'{"delivery_fee": 710}'
    assert response.code == 200