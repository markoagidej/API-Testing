import unittest
from unittest.mock import MagicMock, patch
from app import app
from services.employeeService import save, getAll

class TestEmployeeEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 
        self.app_context = app.app_context() 
        self.app_context.push() 

    @patch('services.employeeService.db.session.query')
    def test_employee_get(self, mock_userList):
        # response = self.app.get('/employees/')
        mock_user = MagicMock()
        mock_user.name = "Test Name"
        mock_user.position = "Test Position"
        mock_user.id = 1
        mock_userList.return_value.all.return_value = [mock_user]

        response = getAll()
        self.assertEqual(response, [mock_user])

    @patch('services.employeeService.db.session.add')
    def test_employee_save(self, mock_employee):
        mock_employee = MagicMock()
        mock_employee.name = "Test Name"
        mock_employee.position = "Test Position"
        mock_employee.id = 1

        response = save({'name': mock_employee.name, 'position': mock_employee.position})
        unittest.assertEqual(response, mock_employee)


        # payload = {"name": "Test Name", "position": "Test Position"}
        # response = self.app.post('/employees/', json=payload)
        # data = response.get_json()
        # print("Here")
        # print(data)
        # print({'name': data['result']['name'], 'position': data['result']['position']})
        # self.assertEqual({'name': data['result']['name'], 'position': data['result']['position']}, {"name": "Test Name", "position": "Test Position"})
        # self.assertEqual(data['result'], {"name": "Test Name", "position": "Test Position", "id":2})

# class TestProductEndpoints(unittest.TestCase):
#     pass

# class TestOrderEndpoints(unittest.TestCase):
#     pass

# class TestCustomerEndpoints(unittest.TestCase):
#     pass

# class TestProductionEndpoints(unittest.TestCase):
#     pass

if __name__ == '__main__':
    unittest.main()