import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services.customerService import save, getAll

class TestCustomerEndpoints(unittest.TestCase):

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

    # Add a customer
    def test_customer_1_save_pass(self):
        mock_customer = MagicMock()
        mock_customer.name = "Test Name"
        mock_customer.email = "test@email.com"
        mock_customer.phone = "123456789"
        mock_customer.id = 1

        response = save({"name": mock_customer.name, "email": mock_customer.email, "phone": mock_customer.phone})
        self.assertEqual({"name": response.name, "email": response.email, "phone": response.phone, "id": response.id}, {"name": mock_customer.name, "email": mock_customer.email, "phone": response.phone, "id": mock_customer.id})

    # Adds another customer
    # This should pass not equals because another customer should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_customer_2_save_fail(self):
        mock_customer = MagicMock()
        mock_customer.name = "Test Name"
        mock_customer.email = "test@email.com"
        mock_customer.phone = "123456789"
        mock_customer.id = 1

        response = save({"name": mock_customer.name, "email": mock_customer.email, "phone": mock_customer.phone})
        self.assertNotEqual({"name": response.name, "email": response.email, "phone": response.phone, "id": response.id}, {"name": mock_customer.name, "email": mock_customer.email, "phone": response.phone, "id": mock_customer.id})

    # Test that the 2 added test customers were added correctly and have expected values
    def test_customer_3_get(self):
        mock_data = [
            {
                "id": 1,
                "name": "Test Name",
                "email": "test@email.com",
                "phone": "123456789"
             },
            {
                "id": 2,
                "name": "Test Name",
                "email": "test@email.com",
                "phone": "123456789"
             }
        ]

        response = getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "name": response[0].name, "email": response[0].email, "phone": response[0].phone}, {"id": response[1].id, "name": response[1].name, "email": response[1].email, "phone": response[1].phone}])

if __name__ == "__main__":
    unittest.main()