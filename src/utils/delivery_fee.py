import os
import sys
from datetime import datetime

try:
    from api_types.calculator import DeliveryFeeRequest
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
    from api_types.calculator import DeliveryFeeRequest


SURCHARGE_BOTTOM = 10 * 100

DISTANCE_INITIAL = 1000
DISTANCE_ADDED = 500
DISTANCE_FEE_INITIAL = 2 * 100
DISTANCE_FEE_ADDED = 1 * 100

ITEM_NUMBER_NO_CHARGE = 4
ITEM_NUMBER_EXTRA_BULK = 12
ITEM_FEE_INITIAL = 0
ITEM_FEE_ADDED = 50
ITEM_FEE_EXTRA_BULK = 1.2 * 100

DELIVERY_FEE_LIMIT = 15 * 100
FREE_DELIVERY_CART_VALUE = 200 * 100

FRIDAY_DAY_NUMBER = 4
FRIDAY_RUSH_TIME_START = 15
FRIDAY_RUSH_TIME_END = 19
FRIDAY_RUSH_MULTIPLIER = 1.2


def small_order_surcharge(cart_value: int) -> int:
    """
    Calculate the surcharge based on the cart value.

    Args:
        cart_value (int): Value of the shopping cart in cents.

    Returns:
        int: The surcharge.
    """
    if cart_value < SURCHARGE_BOTTOM:
        return SURCHARGE_BOTTOM - cart_value
    return 0


def distance_delivery_fee(delivery_distance: int) -> int:
    """
    Calculate the delivery fee based on the delivery distance.

    Args:
        delivery_distance (int): The distance between the store and customer's location in meters.

    Returns:
        int: The delivery based fee.
    """
    if delivery_distance <= DISTANCE_INITIAL:
        return DISTANCE_FEE_INITIAL
    else:
        value = (delivery_distance - DISTANCE_INITIAL) // DISTANCE_ADDED
        b = (delivery_distance - DISTANCE_INITIAL) % DISTANCE_ADDED
        if b > 0:
            return value * DISTANCE_FEE_ADDED + 300
        return value * DISTANCE_FEE_ADDED + DISTANCE_FEE_INITIAL


def item_delivery_fee(number_of_items: int) -> int:
    """
    Calculate the item delivery fee based on the number of items.

    Args:
        number_of_items (int): The number of items in the customer's shopping cart.

    Returns:
        int: The item based fee.
    """
    if number_of_items <= ITEM_NUMBER_NO_CHARGE:
        return ITEM_FEE_INITIAL
    elif ITEM_NUMBER_NO_CHARGE + 1 <= number_of_items <= ITEM_NUMBER_EXTRA_BULK:
        return ITEM_FEE_ADDED * (number_of_items - ITEM_NUMBER_NO_CHARGE)
    else:
        return (number_of_items - ITEM_NUMBER_NO_CHARGE) * ITEM_FEE_ADDED + ITEM_FEE_EXTRA_BULK


def limit_delivery_fee(delivery_fee: int) -> int:
    """
    Limit the delivery fee to a maximum value.

    Args:
        delivery_fee (int): The calculated delivery fee.

    Returns:
        int: The limited delivery fee.
    """
    if delivery_fee > DELIVERY_FEE_LIMIT:
        return DELIVERY_FEE_LIMIT
    return delivery_fee


def is_free_delivery(cart_value) -> bool:
    """
    Check if the delivery exceeds 200€.

    Args:
        cart_value: Value of the shopping cart in cents.

    Returns:
        bool: True if the delivery is free, False otherwise.
    """
    return cart_value >= FREE_DELIVERY_CART_VALUE


def friday_rush_delivery(total_fee: int, time: str) -> int:
    """
    Apply the Friday rush delivery multiplier to the total fee if applicable.

    Args:
        total_fee (int): The total calculated delivery fee.
        time (str): Order time in UTC in ISO format.

    Returns:
        int: The friday rush delivery fee.
    """
    time_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    day_of_the_week = time_object.weekday()
    hour = time_object.hour
    if day_of_the_week == FRIDAY_DAY_NUMBER and FRIDAY_RUSH_TIME_START <= hour <= FRIDAY_RUSH_TIME_END:
        if total_fee * FRIDAY_RUSH_MULTIPLIER >= DELIVERY_FEE_LIMIT:
            return DELIVERY_FEE_LIMIT
        return int(total_fee * FRIDAY_RUSH_MULTIPLIER)
    return total_fee


def delivery_fee(delivery_data: DeliveryFeeRequest) -> int:
    """
    The total delivery fee.

    Args:
        delivery_data (DeliveryFeeRequest): The request data.

    Returns:
        int: The total delivery fee.
    """
    if is_free_delivery(delivery_data.cart_value):
        return 0

    surecharge = small_order_surcharge(delivery_data.cart_value)
    distance_fee = distance_delivery_fee(delivery_data.delivery_distance)
    items_fee = item_delivery_fee(delivery_data.number_of_items)
    friday_rush_delivery_fee = friday_rush_delivery(surecharge+distance_fee+items_fee, delivery_data.time)
    fee = limit_delivery_fee(friday_rush_delivery_fee)

    return fee
