import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services import employeeService
from services import productService
from services import customerService
from services import orderService
from services import productionService
from datetime import date

class TestAllEndpoints(unittest.TestCase):

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

    # Add an employee
    def test_01_employee_1_save_pass(self):
        mock_employee = MagicMock()
        mock_employee.name = "Test Name"
        mock_employee.position = "Test Position"
        mock_employee.id = 1

        response = employeeService.save({"name": mock_employee.name, "position": mock_employee.position})
        self.assertEqual({"name": response.name, "position": response.position, "id": response.id}, {"name": mock_employee.name, "position": mock_employee.position, "id": mock_employee.id})

    # Adds another employee
    # This should pass not equals because another employee should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_02_employee_2_save_fail(self):
        mock_employee = MagicMock()
        mock_employee.name = "Test Name"
        mock_employee.position = "Test Position"
        mock_employee.id = 1

        response = employeeService.save({"name": mock_employee.name, "position": mock_employee.position})
        self.assertNotEqual({"name": response.name, "position": response.position, "id": response.id}, {"name": mock_employee.name, "position": mock_employee.position, "id": mock_employee.id})

    # Test that the 2 added test employees were added correctly and have expected values
    def test_03_employee_3_get(self):
        mock_data = [
            {
                "id": 1,
                "name": "Test Name",
                "position": "Test Position"
             },
            {
                "id": 2,
                "name": "Test Name",
                "position": "Test Position"
             }
        ]

        response = employeeService.getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "name": response[0].name, "position": response[0].position}, {"id": response[1].id, "name": response[1].name, "position": response[1].position}])
    
    # Add a product
    def test_04_product_1_save_pass(self):
        mock_product = MagicMock()
        mock_product.name = "Test Name"
        mock_product.price = 1.01
        mock_product.id = 1

        response = productService.save({'name': mock_product.name, 'price': mock_product.price})
        self.assertEqual({"name": response.name, "price": response.price, "id": response.id}, {"name": mock_product.name, "price": mock_product.price, "id": mock_product.id})

    # Adds another product
    # This should pass not equals because another product should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_05_product_2_save_fail(self):
        mock_product = MagicMock()
        mock_product.name = "Test Name"
        mock_product.price = 1.01
        mock_product.id = 1

        response = productService.save({'name': mock_product.name, 'price': mock_product.price})
        self.assertNotEqual({"name": response.name, "price": response.price, "id": response.id}, {"name": mock_product.name, "price": mock_product.price, "id": mock_product.id})

    # Test that the 2 added test products were added correctly and have expected values
    def test_06_product_3_get(self):
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

        response = productService.getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "name": response[0].name, "price": response[0].price}, {"id": response[1].id, "name": response[1].name, "price": response[1].price}])

    # Add a customer
    def test_07_customer_1_save_pass(self):
        mock_customer = MagicMock()
        mock_customer.name = "Test Name"
        mock_customer.email = "test@email.com"
        mock_customer.phone = "123456789"
        mock_customer.id = 1

        response = customerService.save({"name": mock_customer.name, "email": mock_customer.email, "phone": mock_customer.phone})
        self.assertEqual({"name": response.name, "email": response.email, "phone": response.phone, "id": response.id}, {"name": mock_customer.name, "email": mock_customer.email, "phone": response.phone, "id": mock_customer.id})

    # Adds another customer
    # This should pass not equals because another customer should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_08_customer_2_save_fail(self):
        mock_customer = MagicMock()
        mock_customer.name = "Test Name"
        mock_customer.email = "test@email.com"
        mock_customer.phone = "123456789"
        mock_customer.id = 1

        response = customerService.save({"name": mock_customer.name, "email": mock_customer.email, "phone": mock_customer.phone})
        self.assertNotEqual({"name": response.name, "email": response.email, "phone": response.phone, "id": response.id}, {"name": mock_customer.name, "email": mock_customer.email, "phone": response.phone, "id": mock_customer.id})

    # Test that the 2 added test customers were added correctly and have expected values
    def test_09_customer_3_get(self):
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

        response = customerService.getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "name": response[0].name, "email": response[0].email, "phone": response[0].phone}, {"id": response[1].id, "name": response[1].name, "email": response[1].email, "phone": response[1].phone}])

    # Add a order
    def test_10_order_1_save_pass(self):
        mock_order = MagicMock()
        mock_order.customer_id = 1
        mock_order.product_id = 1
        mock_order.quantity = 5
        mock_order.total_price = 10

        response = orderService.save({"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})
        self.assertEqual({"customer_id": response.customer_id, "product_id": response.product_id, "quantity": response.quantity, "total_price": response.total_price}, {"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})

    # Adds another order
    # This should pass not equals because another order should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_11_order_2_save_fail(self):
        mock_order = MagicMock()
        mock_order.customer_id = 1
        mock_order.product_id = 1
        mock_order.quantity = 5
        mock_order.total_price = 10
        mock_order.id = 1

        response = orderService.save({"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price})
        self.assertNotEqual({"customer_id": response.customer_id, "product_id": response.product_id, "quantity": response.quantity, "total_price": response.total_price, "id": response.id}, {"customer_id": mock_order.customer_id, "product_id": mock_order.product_id, "quantity": mock_order.quantity, "total_price": mock_order.total_price, "id": mock_order.id})

    # Test that the 2 added test orders were added correctly and have expected values
    def test_12_order_3_get(self):
        mock_data = [
            {
                "id": 1,
                "quantity": 5,
                "customer_id": 1,
                "product_id": 1,
                "total_price": 10
             },
            {
                "id": 2,
                "quantity": 5,
                "customer_id": 1,
                "product_id": 1,
                "total_price": 10
             }
        ]

        response = orderService.getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "quantity": response[0].quantity, "customer_id": response[0].customer_id, "product_id": response[0].product_id, "total_price": response[0].total_price}, {"id": response[1].id, "quantity": response[1].quantity, "customer_id": response[1].customer_id, "product_id": response[1].product_id, "total_price": response[1].total_price}])

    # Add a production
    def test_13_production_1_save_pass(self):
        mock_production = MagicMock()
        mock_production.product_id = 1
        mock_production.quantity_produced = 10
        mock_production.date_produced = date(2024, 9, 6)

        response = productionService.save({"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})
        self.assertEqual({"product_id": response.product_id, "quantity_produced": response.quantity_produced, "date_produced": response.date_produced}, {"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})

    # Adds another production
    # This should pass not equals because another production should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_14_production_2_save_fail(self):
        mock_production = MagicMock()
        mock_production.product_id = 1
        mock_production.quantity_produced = 10
        mock_production.date_produced = date(2024, 9, 6)
        mock_production.id = 1

        response = productionService.save({"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced})
        self.assertNotEqual({"product_id": response.product_id, "quantity_produced": response.quantity_produced, "date_produced": response.date_produced, "id":response.id}, {"product_id": mock_production.product_id, "quantity_produced": mock_production.quantity_produced, "date_produced": mock_production.date_produced, "id":mock_production.id})

    # Test that the 2 added test productions were added correctly and have expected values
    def test_15_production_3_get(self):
        mock_data = [
            {
                "id": 1,
                "date_produced": date(2024, 9, 6),
                "product_id": 1,
                "quantity_produced": 10
             },
            {
                "id": 2,
                "date_produced": date(2024, 9, 6),
                "product_id": 1,
                "quantity_produced": 10
             }
        ]

        response = productionService.getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "date_produced": response[0].date_produced, "product_id": response[0].product_id, "quantity_produced": response[0].quantity_produced}, {"id": response[1].id, "date_produced": response[1].date_produced, "product_id": response[1].product_id, "quantity_produced": response[1].quantity_produced}])

if __name__ == "__main__":
    unittest.main()