import unittest
from fastapi.testclient import TestClient
from main import app


class TestCartAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    # Define a test case for a valid request
    def test_valid_request(self):
        request = {
            "cart_value": 1,
            "delivery_distance": 1,
            "number_of_items": 1,
            "time": "2024-01-15T13:00:00Z",
        }
        expected_response = {"delivery_fee": 1199}

        response = self.client.post("/cart/calculate-delivery-fee", json=request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    # Define a test case for an invalid cart_value, delivery_distance, number_of_items
    def test_invalid_value(self):
        request = {
            "cart_value": -1,
            "delivery_distance": -1,
            "number_of_items": -1,
            "time": "2024-01-15T13:00:00Z",
        }
        expected_response = {
            "detail": [
                {
                    "loc": ["body", "cart_value"],
                    "msg": "Input should be greater than or equal to 0",
                },
                {
                    "loc": ["body", "delivery_distance"],
                    "msg": "Input should be greater than or equal to 0",
                },
                {
                    "loc": ["body", "number_of_items"],
                    "msg": "Input should be greater than or equal to 0",
                },
            ]
        }

        response = self.client.post("/cart/calculate-delivery-fee", json=request)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            len(response.json()["detail"]), len(expected_response["detail"])
        )
        self.assertEqual(
            response.json()["detail"][0]["loc"], expected_response["detail"][0]["loc"]
        )
        self.assertEqual(
            response.json()["detail"][0]["msg"], expected_response["detail"][0]["msg"]
        )

    # Define a test case for an invalid time format
    def test_invalid_time_format(self):
        request = {
            "cart_value": 1,
            "delivery_distance": 1,
            "number_of_items": 1,
            "time": "2024-01-15",
        }
        expected_response = {"detail": "Invalid isoformat string:"}

        response = self.client.post("/cart/calculate-delivery-fee", json=request)
        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_response["detail"], response.json()["detail"])


if __name__ == "__main__":
    unittest.main()
