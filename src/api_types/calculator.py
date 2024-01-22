from dataclasses import dataclass


@dataclass
class DeliveryFeeRequest:
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str