import os
import sys
from dacite import from_dict


try:
    from src.utils.delivery_fee import *
    from src.api_types.calculator import DeliveryFeeRequest
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
    from src.utils.delivery_fee import *
    from src.api_types.calculator import DeliveryFeeRequest


def test_small_order_surcharge(mock_delivery_data, mock_surcharge):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert small_order_surcharge(delivery_data.cart_value) == mock_surcharge[i]


def test_distance_delivery_fee(mock_delivery_data, mock_distance_fee):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert distance_delivery_fee(delivery_data.delivery_distance) == mock_distance_fee[i]


def test_item_delivery_fee(mock_delivery_data, mock_item_fee):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert item_delivery_fee(delivery_data.number_of_items) == mock_item_fee[i]

def test_is_free_delivery(mock_delivery_data, mock_is_free_delivery):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert is_free_delivery(delivery_data.cart_value) == mock_is_free_delivery[i]


def test_friday_rush_delivery(mock_delivery_data, mock_friday_rush_fee):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        surcharge = small_order_surcharge(delivery_data.cart_value)
        distance_fee = distance_delivery_fee(delivery_data.delivery_distance)
        item_fee = item_delivery_fee(delivery_data.number_of_items)
        assert friday_rush_delivery(surcharge+distance_fee+item_fee, delivery_data.time) == mock_friday_rush_fee[i]


def test_delivery_fee_calculator(mock_delivery_data, mock_delivery_fee):
   for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert delivery_fee(delivery_data) == mock_delivery_fee[i]


def test_delivery_fee_calculator_failed(mock_delivery_data, mock_delivery_fee):
   for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert delivery_fee(delivery_data) != -1