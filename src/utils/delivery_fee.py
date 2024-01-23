import os
import sys
from datetime import datetime

try:
    from api_types.calculator import DeliveryFeeRequest
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
    from api_types.calculator import DeliveryFeeRequest

from dacite import from_dict


def small_order_surcharge(cart_value: int) -> int:
    if cart_value < 1000:
        return 1000 - cart_value
    return 0


def distance_delivery_fee(delivery_distance: int) -> int:
    if delivery_distance <= 1000:
        return 200
    else:
        value = (delivery_distance - 1000) // 500
        b = (delivery_distance - 1000) % 500
        if b > 0:
            return value * 100 + 300
        return value


def item_delivery_fee(number_of_items: int) -> int:
    if number_of_items <= 4:
        return 0
    elif 5 <= number_of_items <= 12:
        return 50 * (number_of_items - 4)
    else:
        return (number_of_items - 4) * 50 + 1.2 * 100


def limit_delivery_fee(delivery_fee: int) -> int:
    if delivery_fee > 1500:
        return 1500
    return delivery_fee


def is_free_delivery(cart_value) -> bool:
    return cart_value >= 20000


def friday_rush_delivery(total_fee: int, time: str) -> int:
    time_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    day_of_the_week = time_object.weekday()
    hour = time_object.hour
    print(day_of_the_week, hour)
    if day_of_the_week == 4 and 15 <= hour <= 19:
        if total_fee * 1.2 >= 1500:
            return 1500
        return int(total_fee * 1.2)
    return total_fee


def delivery_fee(delivery_data: DeliveryFeeRequest) -> int:

    if is_free_delivery(delivery_data.cart_value):
        return 0

    surecharge = small_order_surcharge(delivery_data.cart_value)
    distance_fee = distance_delivery_fee(delivery_data.delivery_distance)
    items_fee = item_delivery_fee(delivery_data.number_of_items)
    friday_rush_delivery_fee = friday_rush_delivery(surecharge+distance_fee+items_fee, delivery_data.time)

    return friday_rush_delivery_fee


if __name__ == '__main__':
    data = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 5,
        "time": "2024-01-19T15:00:00Z"
    }
    delivery_fee_data = from_dict(data_class=DeliveryFeeRequest, data=data)
    print(delivery_fee(delivery_fee_data))
