import os
import sys
from datetime import datetime

try:
    from api_types.calculator import DeliveryFeeRequest
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
    from api_types.calculator import DeliveryFeeRequest


def small_order_surcharge(cart_value: int) -> int:
    """
    Calculate the surcharge based on the cart value.

    Args:
        cart_value (int): Value of the shopping cart in cents.

    Returns:
        int: The surcharge.
    """
    if cart_value < 1000:
        return 1000 - cart_value
    return 0


def distance_delivery_fee(delivery_distance: int) -> int:
    """
    Calculate the delivery fee based on the delivery distance.

    Args:
        delivery_distance (int): The distance between the store and customer's location in meters.

    Returns:
        int: The delivery based fee.
    """
    if delivery_distance <= 1000:
        return 200
    else:
        value = (delivery_distance - 1000) // 500
        b = (delivery_distance - 1000) % 500
        if b > 0:
            return value * 100 + 300
        return value * 100 + 200


def item_delivery_fee(number_of_items: int) -> int:
    """
    Calculate the item delivery fee based on the number of items.

    Args:
        number_of_items (int): The number of items in the customer's shopping cart.

    Returns:
        int: The item based fee.
    """
    if number_of_items <= 4:
        return 0
    elif 5 <= number_of_items <= 12:
        return 50 * (number_of_items - 4)
    else:
        return (number_of_items - 4) * 50 + 1.2 * 100


def limit_delivery_fee(delivery_fee: int) -> int:
    """
    Limit the delivery fee to a maximum value.

    Args:
        delivery_fee (int): The calculated delivery fee.

    Returns:
        int: The limited delivery fee.
    """
    if delivery_fee > 1500:
        return 1500
    return delivery_fee


def is_free_delivery(cart_value) -> bool:
    """
    Check if the delivery exceeds 200€.

    Args:
        cart_value: Value of the shopping cart in cents.

    Returns:
        bool: True if the delivery is free, False otherwise.
    """
    return cart_value >= 20000


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
    if day_of_the_week == 4 and 15 <= hour <= 19:
        if total_fee * 1.2 >= 1500:
            return 1500
        return int(total_fee * 1.2)
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
