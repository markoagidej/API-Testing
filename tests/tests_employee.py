import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services.employeeService import save, getAll

class TestEmployeeEndpoints(unittest.TestCase):

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
    def test_employee_1_save_pass(self):
        mock_employee = MagicMock()
        mock_employee.name = "Test Name"
        mock_employee.position = "Test Position"
        mock_employee.id = 1

        response = save({"name": mock_employee.name, "position": mock_employee.position})
        self.assertEqual({"name": response.name, "position": response.position, "id": response.id}, {"name": mock_employee.name, "position": mock_employee.position, "id": mock_employee.id})

    # Adds another employee
    # This should pass not equals because another employee should already be in the mock db, thus the new entry id is 2 not 1 (file runs tests alphabetically)
    def test_employee_2_save_fail(self):
        mock_employee = MagicMock()
        mock_employee.name = "Test Name"
        mock_employee.position = "Test Position"
        mock_employee.id = 1

        response = save({"name": mock_employee.name, "position": mock_employee.position})
        self.assertNotEqual({"name": response.name, "position": response.position, "id": response.id}, {"name": mock_employee.name, "position": mock_employee.position, "id": mock_employee.id})

    # Test that the 2 added test employees were added correctly and have expected values
    def test_employee_3_get(self):
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

        response = getAll()
        self.assertEqual(mock_data, [{"id": response[0].id, "name": response[0].name, "position": response[0].position}, {"id": response[1].id, "name": response[1].name, "position": response[1].position}])

if __name__ == "__main__":
    unittest.main()