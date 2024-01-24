import os
import sys
import pytest

try:
    from src.main import Server
    from src.api_types.calculator import DeliveryFeeRequest
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
    from src.main import Server
    from src.api_types.calculator import DeliveryFeeRequest


@pytest.fixture
def app():
    app = Server(PORT=8888)
    return app.get_app()

@pytest.fixture
def mock_delivery_data() -> list[DeliveryFeeRequest]:
    return [
        {"cart_value": 890, "delivery_distance": 500, "number_of_items": 2, "time": "2024-01-15T10:00:00Z"},
        {"cart_value": 1000, "delivery_distance": 700, "number_of_items": 3, "time": "2024-01-15T11:00:00Z"},
        {"cart_value": 2000, "delivery_distance": 1500, "number_of_items": 6, "time": "2024-01-15T12:00:00Z"},
        {"cart_value": 25000, "delivery_distance": 1000, "number_of_items": 5, "time": "2024-01-15T14:00:00Z"},
        {"cart_value": 1500, "delivery_distance": 1200, "number_of_items": 8, "time": "2024-01-17T16:00:00Z"},
        {"cart_value": 1500, "delivery_distance": 800, "number_of_items": 4, "time": "2024-01-17T14:00:00Z"},
        {"cart_value": 500, "delivery_distance": 3000, "number_of_items": 15, "time": "2024-01-15T15:00:00Z"},
        {"cart_value": 20000, "delivery_distance": 1200, "number_of_items": 7, "time": "2024-01-15T16:00:00Z"},
        {"cart_value": 5000, "delivery_distance": 1500, "number_of_items": 3, "time": "2024-01-15T17:00:00Z"},
        {"cart_value": 3000, "delivery_distance": 500, "number_of_items": 2, "time": "2024-01-15T18:00:00Z"},
        {"cart_value": 1500, "delivery_distance": 800, "number_of_items": 4, "time": "2024-01-17T19:00:00Z"},
        {"cart_value": 850, "delivery_distance": 2500, "number_of_items": 2, "time": "2024-01-15T20:00:00Z"},
        {"cart_value": 1500, "delivery_distance": 200, "number_of_items": 1, "time": "2024-01-15T21:00:00Z"},
        {"cart_value": 3000, "delivery_distance": 800, "number_of_items": 13, "time": "2024-01-15T22:00:00Z"},
        {"cart_value": 50000, "delivery_distance": 1000, "number_of_items": 5, "time": "2024-01-15T23:00:00Z"},
        {"cart_value": 4000, "delivery_distance": 1200, "number_of_items": 6, "time": "2024-01-17T15:30:00Z"},
        {"cart_value": 550, "delivery_distance": 1000, "number_of_items": 3, "time": "2024-01-15T14:30:00Z"},
        {"cart_value": 1200, "delivery_distance": 500, "number_of_items": 2, "time": "2024-01-15T16:30:00Z"},
        {"cart_value": 7000, "delivery_distance": 2000, "number_of_items": 15, "time": "2024-01-17T16:30:00Z"},
        {"cart_value": 2500, "delivery_distance": 3000, "number_of_items": 8, "time": "2024-01-17T17:30:00Z"},
        {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
    ]

@pytest.fixture
def mock_surcharge() -> list[int]:
    return [110, 0, 0, 0, 0, 0, 500, 0, 0, 0, 0, 150, 0, 0, 0, 0, 450, 0, 0, 0, 210]

@pytest.fixture
def mock_distance_fee() -> list[int]:
    return [200, 200, 300, 200, 300, 200, 600, 300, 300, 200, 200, 500, 200, 200, 200, 300, 200, 200, 400, 600, 500]

@pytest.fixture
def mock_item_fee() -> list[int]:
    return [0, 0, 100, 50, 200, 0, 670, 150, 0, 0, 0, 0, 0, 570, 50, 100, 0, 0, 670, 200, 0]

@pytest.fixture
def mock_is_free_delivery() -> list[bool]:
    return [False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False]

@pytest.fixture
def mock_friday_rush_fee() -> list[int]:
    return [310, 200, 400, 250, 500, 200, 1770, 450, 300, 200, 200, 650, 200, 770, 250, 400, 650, 200, 1070, 800, 710]

@pytest.fixture
def mock_delivery_fee() -> list[int]:
    return [310, 200, 400, 0, 500, 200, 1500, 0, 300, 200, 200, 650, 200, 770, 0, 400, 650, 200, 1070, 800, 710]

@pytest.fixture
def mock_payload() -> DeliveryFeeRequest:
    return {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
