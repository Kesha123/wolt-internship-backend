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
        value = small_order_surcharge(delivery_data.cart_value)
        assert value == mock_surcharge[i] and type(value) == int


def test_distance_delivery_fee(mock_delivery_data, mock_distance_fee):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        value = distance_delivery_fee(delivery_data.delivery_distance)
        assert value == mock_distance_fee[i] and type(value) == int


def test_item_delivery_fee(mock_delivery_data, mock_item_fee):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        value = item_delivery_fee(delivery_data.number_of_items)
        assert value == mock_item_fee[i] and type(value) == int


def test_is_free_delivery(mock_delivery_data, mock_is_free_delivery):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        value = is_free_delivery(delivery_data.cart_value)
        assert value  == mock_is_free_delivery[i] and type(value) == bool


def test_friday_rush_delivery(mock_delivery_data, mock_friday_rush_fee):
    for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        surcharge = small_order_surcharge(delivery_data.cart_value)
        distance_fee = distance_delivery_fee(delivery_data.delivery_distance)
        item_fee = item_delivery_fee(delivery_data.number_of_items)
        value = friday_rush_delivery(surcharge+distance_fee+item_fee, delivery_data.time)
        assert value == mock_friday_rush_fee[i] and type(value) == int


def test_delivery_fee_calculator(mock_delivery_data, mock_delivery_fee):
   for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        value = delivery_fee(delivery_data)
        assert value == mock_delivery_fee[i] and type(value) == int


def test_delivery_fee_calculator_failed(mock_delivery_data, mock_delivery_fee):
   for i, data in enumerate(mock_delivery_data):
        delivery_data = from_dict(data_class=DeliveryFeeRequest, data=data)
        assert delivery_fee(delivery_data) != -1