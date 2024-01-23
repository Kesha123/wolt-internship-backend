import os
import sys
import json
import pytest

from conftest import mock_payload

try:
    from src.main import Server
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
    from main import Server


@pytest.fixture
def app():
    app = Server(PORT=8888)
    return app.get_app()


@pytest.mark.gen_test
def test_api_health(http_client, base_url, mock_payload):
    response = yield http_client.fetch(
            f"{base_url}/api/delivery-fee-calculator",
            method="POST",
            body=json.dumps(mock_payload)
        )
    assert response.code == 200