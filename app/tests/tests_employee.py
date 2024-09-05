import unittest
from unittest.mock import MagicMock, patch
from app import create_app, db
from services.employeeService import save, getAll

class TestEmployeeEndpoints(unittest.TestCase):

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

    # @patch('services.employeeService.db.session.query')
    # def test_employee_get(self, mock_query):
    #     mock_user = MagicMock()
    #     mock_user.name = "Test Name"
    #     mock_user.position = "Test Position"
    #     mock_user.id = 1
    #     mock_query.return_value.all.return_value = [mock_user]
    #     print(mock_user)

    #     # Test the getAll function
    #     response = getAll()
    #     print("RESPONSE")
    #     print(response)
    #     self.assertEqual(response, [mock_user])

    @patch('services.employeeService.db.session.add')
    @patch('services.employeeService.db.session.commit')
    def test_employee_save(self, mock_commit, mock_add):
        mock_employee = MagicMock()
        mock_employee.name = "Test Name"
        mock_employee.position = "Test Position"
        mock_employee.id = 1
        # mock_add.return_value = mock_employee

        response = save({'name': mock_employee.name, 'position': mock_employee.position})
        # breakpoint()
        print(f"RESPONSE: {response}")
        self.assertEqual({"id": response.id, "name": response.name}, mock_employee.id)

if __name__ == '__main__':
    unittest.main()