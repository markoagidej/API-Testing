import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services.productService import save, getAll

class TestProductEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('DevelopmentConfig') 
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

    # Add a product
    def test_product_1_save_pass(self):
        mock_product = MagicMock()
        mock_product.name = "Test Name"
        mock_product.price = 1.01
        mock_product.id = 1

        response = save({'name': mock_product.name, 'price': mock_product.price})
        self.assertEqual({"name": response.name, "price": response.price, "id": response.id}, {"name": mock_product.name, "price": mock_product.price, "id": mock_product.id})

    # Adds another product
    # This should pass not equals because another product should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_product_2_save_fail(self):
        mock_product = MagicMock()
        mock_product.name = "Test Name"
        mock_product.price = 1.01
        mock_product.id = 1

        response = save({'name': mock_product.name, 'price': mock_product.price})
        self.assertNotEqual({"name": response.name, "price": response.price, "id": response.id}, {"name": mock_product.name, "price": mock_product.price, "id": mock_product.id})

    # Test that the 2 added test products were added correctly and have expected values
    def test_product_3_get(self):
        mock_data = [
            {
                "id": 1,
                "name": "Test Name",
                "price": 1.01
             },
            {
                "id": 2,
                "name": "Test Name",
                "price": 1.01
             }
        ]

        response = getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "name": response[0].name, "price": response[0].price}, {"id": response[1].id, "name": response[1].name, "price": response[1].price}])

if __name__ == '__main__':
    unittest.main()