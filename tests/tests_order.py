import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services.orderService import save, getAll

class TestOrderEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app("DevelopmentConfig") 
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()
        cls.app_context.pop()

    # Add a order
    def test_order_1_save_pass(self):
        mock_order = MagicMock()
        mock_order.customer_id = 1
        mock_order.product_id = 1
        mock_order.quantity = 5
        mock_order.total_price = 10

        response = save({"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})
        self.assertEqual({"customer_id": response.customer_id, "product_id": response.product_id, "quantity": response.quantity, "total_price": response.total_price}, {"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})

    # Adds another order
    # This should pass not equals because another order should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_order_2_save_fail(self):
        mock_order = MagicMock()
        mock_order.customer_id = 1
        mock_order.product_id = 1
        mock_order.quantity = 5
        mock_order.total_price = 10

        response = save({"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})
        self.assertNotEqual({"customer_id": response.customer_id, "product_id": response.product_id, "quantity": response.quantity, "total_price": response.total_price}, {"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})

    # Test that the 2 added test orders were added correctly and have expected values
    def test_order_3_get(self):
        mock_data = [
            {
                "quantity": 5,
                "customer_id": 1,
                "product_id": 1,
                "total_price": 10
             },
            {
                "quantity": 5,
                "customer_id": 1,
                "product_id": 1,
                "total_price": 10
             }
        ]

        response = getAll()
        self.assertEqual(mock_data, [{"quantity": response[0].quantity, "customer_id": response[0].customer_id, "product_id": response[0].product_id, "total_price": response[0].total_price}, {"quantity": response[1].quantity, "customer_id": response[1].customer_id, "product_id": response[1].product_id, "total_price": response[1].total_price}])

if __name__ == "__main__":
    unittest.main()