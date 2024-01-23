from datetime import datetime


def small_order_surcharge(cart_value: int) -> int:
    if cart_value < 1000:
        return 1000 - cart_value
    return 0


def distance_delivery_fee(delivery_distance: int) -> int:
    if delivery_distance <= 1000:
        return 2
    else:
        value = (delivery_distance - 1000) // 500
        b = (delivery_distance - 1000) % 500
        if b > 0:
            return value + 1
        return value


def item_delivery_fee(number_of_items: int) -> int:
    if number_of_items <= 4:
        return 0
    elif 5 <= number_of_items <= 12:
        return 50 * number_of_items
    else:
        return (number_of_items - 4) * 50 + 1.2 * 100


def limit_delivery_fee(delivery_fee: int) -> int:
    if delivery_fee > 15:
        return 15
    return delivery_fee


def is_free_delivery(cart_value) -> bool:
    return cart_value >= 200


def friday_rush_delivery(total_fee: int, time: str) -> int:
    time_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    day_of_the_week = time_object.weekday()
    hour = time_object.hour
    if day_of_the_week == 5 and 15 <= hour <= 19:
        if total_fee * 1.2 >= 1500:
            return 1500
        return total_fee * 1.2
