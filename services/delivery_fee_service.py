import math, datetime

FREE_DELIVERY_THRESHOLD = 20000
SURCHARGE_THRESHOLD = 1000
BASE_FEE = 200
DISTANCE_THRESHOLD = 1000
ADDITIONAL_DISTANCE_FEE_UNIT = 100
ITEM_SURCHARGE_UNIT = 50
BULK_FEE = 120
BULK_ITEM_THRESHOLD = 12
FRIDAY_RUSH_START = 15  # 3 PM UTC
FRIDAY_RUSH_END = 19  # 7 PM UTC
MAX_FEE = 1500


class DeliveryFeeCalculator:
    def __init__(
        self, cart_value: int, delivery_distance: int, number_of_items: int, time: str
    ):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time

    def calculate_fee(self) -> int:
        """Calculate total delivery fee."""
        if self.cart_value >= FREE_DELIVERY_THRESHOLD:
            return 0

        surcharge = self.calculate_surcharge()
        distance_fee = self.calculate_distance_fee()
        total_items_surcharge = self.calculate_items_surcharge()
        delivery_fee = surcharge + distance_fee + total_items_surcharge

        delivery_fee = self.apply_friday_rush_multiplier(delivery_fee)
        delivery_fee = self.cap_delivery_fee(delivery_fee)

        return round(delivery_fee)

    def calculate_surcharge(self):
        """Calculate surcharge based on cart value."""
        return (
            SURCHARGE_THRESHOLD - self.cart_value
            if self.cart_value < SURCHARGE_THRESHOLD
            else 0
        )

    def calculate_distance_fee(self):
        """Calculate distance fee based on delivery distance."""
        distance_fee = BASE_FEE
        if self.delivery_distance > DISTANCE_THRESHOLD:
            distance_fee += (
                math.ceil((self.delivery_distance - DISTANCE_THRESHOLD) / 500)
                * ADDITIONAL_DISTANCE_FEE_UNIT
            )
        return distance_fee

    def calculate_items_surcharge(self):
        """Calculate items surcharge based on number of items."""
        total_items_surcharge = 0
        if self.number_of_items >= 5:
            total_items_surcharge += (self.number_of_items - 4) * ITEM_SURCHARGE_UNIT
            if self.number_of_items > BULK_ITEM_THRESHOLD:
                total_items_surcharge += BULK_FEE
        return total_items_surcharge

    def apply_friday_rush_multiplier(self, delivery_fee):
        """Apply Friday rush multiplier if it's Friday rush hour."""
        utc_datetime = datetime.datetime.fromisoformat(
            self.time[:-1]
        )  # [:-1] to avoid the Z at the end of the string which causes "Invalid isoformat string" for python version < 3.11
        if (
            utc_datetime.weekday() == 4
            and FRIDAY_RUSH_START <= utc_datetime.hour <= FRIDAY_RUSH_END
        ):  # 4 is Friday
            delivery_fee *= 1.2
        return delivery_fee

    def cap_delivery_fee(self, delivery_fee):
        """Cap the delivery fee to the maximum fee."""
        return min(delivery_fee, MAX_FEE)
