import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services.productionService import save, getAll
from datetime import datetime

class TestProductionEndpoints(unittest.TestCase):

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

    # Add a production
    def test_production_1_save_pass(self):
        mock_production = MagicMock()
        mock_production.product_id = 1
        mock_production.quantity_produced = 10
        mock_production.date_produced = datetime(2024, 9, 6, 2, 30)

        response = save({"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})
        self.assertEqual({"product_id": response.product_id, "quantity_produced": response.quantity_produced, "date_produced": response.date_produced}, {"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})

    # Adds another production
    # This should pass not equals because another production should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_production_2_save_fail(self):
        mock_production = MagicMock()
        mock_production.product_id = 1
        mock_production.quantity_produced = 10
        mock_production.date_produced = datetime(2024, 9, 6, 2, 30)

        response = save({"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})
        self.assertNotEqual({"product_id": response.product_id, "quantity_produced": response.quantity_produced, "date_produced": response.date_produced}, {"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})

    # Test that the 2 added test productions were added correctly and have expected values
    def test_production_3_get(self):
        mock_data = [
            {
                "id": 1,
                "date_produced": datetime(2024, 9, 6, 2, 30),
                "product_id": 1,
                "quantity_produced": 10
             },
            {
                "id": 2,
                "date_produced": datetime(2024, 9, 6, 2, 30),
                "product_id": 1,
                "quantity_produced": 10
             }
        ]

        response = getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "date_produced": response[0].date_produced, "product_id": response[0].product_id, "quantity_produced": response[0].quantity_produced}, {"id": response[1].id, "date_produced": response[1].date_produced, "product_id": response[1].product_id, "quantity_produced": response[1].quantity_produced}])

if __name__ == "__main__":
    unittest.main()