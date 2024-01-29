import unittest
from services.delivery_fee_service import DeliveryFeeCalculator


class TestDeliveryFeeCalculator(unittest.TestCase):
    def test_calculate_surcharge(self):
        calc = DeliveryFeeCalculator(890, 1000, 5, "2024-01-15T13:00:00Z")
        self.assertEqual(calc.calculate_surcharge(), 110)

    def test_calculate_distance_fee(self):
        calc = DeliveryFeeCalculator(1000, 1501, 5, "2024-01-15T13:00:00Z")
        self.assertEqual(calc.calculate_distance_fee(), 400)

    def test_calculate_items_surcharge(self):
        calc = DeliveryFeeCalculator(1000, 1000, 14, "2024-01-15T13:00:00Z")
        self.assertEqual(calc.calculate_items_surcharge(), 620)

    def test_apply_friday_rush_multiplier(self):
        calc = DeliveryFeeCalculator(
            1000, 1000, 5, "2024-01-26T18:00:00Z"
        )  # It's Friday rush hour
        self.assertEqual(calc.apply_friday_rush_multiplier(1000), 1200)

    def test_cap_delivery_fee(self):
        calc = DeliveryFeeCalculator(1000, 1000, 5, "2024-01-15T13:00:00Z")
        self.assertEqual(calc.cap_delivery_fee(2000), 1500)

    def test_calculate_fee(self):
        calc = DeliveryFeeCalculator(
            1000, 15010, 14, "2024-01-26T18:00:00Z"
        )  # It's Friday rush hour
        self.assertEqual(calc.calculate_fee(), 1500)  # The fee is capped at 15


if __name__ == "__main__":
    unittest.main()
