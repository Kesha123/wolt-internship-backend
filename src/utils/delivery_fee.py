from datetime import datetime
from api_types.calculator import DeliveryFeeRequest

SURCHARGE = 10 * 100
FREE_DELIVERY_DISTANCE = 1000
DISTANCE_BASED_DELIVERY_FEE = 2
ADDITIONAL_DISTANCE_FEE = 1 * 100
MAXIMUM_DELIVERY_FEE = 15 * 100
FREE_DELIVERY_CART_VALUE = 200 * 100
FRIDAY_RUSH_COEFFICIENT = 1.2


def small_order_surcharge(delivery_data: DeliveryFeeRequest) -> int:
    if delivery_data.cart_value < SURCHARGE:
        return SURCHARGE - delivery_data.cart_value
    return 0


def distance_delivery_fee(delivery_data: DeliveryFeeRequest) -> int:
    if delivery_data.delivery_distance <= 1000:
        return 2
    else:
        value = (delivery_data.delivery_distance - 1000) // 500
        b = (delivery_data.delivery_distance - 1000) % 500
        if b > 0:
            return value + 1
        return value


def item_delivery_fee(delivery_data: DeliveryFeeRequest) -> int:
    if delivery_data.number_of_items <= 4:
        return 0
    elif 5 <= delivery_data.number_of_items <= 12:
        return 50 * delivery_data.number_of_items
    else:
        return (delivery_data.nnumber_of_items - 4) * 50 + 1.2 * 100


def limit_delivery_fee(delivery_fee: int) -> int:
    if delivery_fee > 15:
        return 15
    return delivery_fee


def is_free_delivery(delivery_data: DeliveryFeeRequest) -> bool:
    return delivery_data.cart_value >= 200


def friday_rush_delivery(total_fee: int, time: str) -> int:
    time_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    day_of_the_week = time_object.weekday()
    hour = time_object.hour
    if day_of_the_week == 5 and 15 <= hour <= 19:
        return