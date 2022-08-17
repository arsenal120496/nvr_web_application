import unittest
from service.user import *
from app import app

# additional API testing in postman
class FlaskTest(unittest.TestCase):
    # Test route /user/getList
    # Check for response 200
    def test_getList_response(self):
        tester = app.test_client(self)
        response = tester.get('/user/getList')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content return is application/json
    def test_getList_content(self):
        tester = app.test_client(self)
        response = tester.get('/user/getList')
        self.assertEqual(response.content_type, "application/json")

    # Test route /user/query/<id>
    def test_query_response_1(self):
        tester = app.test_client(self)
        response = tester.get('/user/query/0')
        statuscode = response.status_code
        self.assertEqual(statuscode, 203)

    # assuming database has at least 1 User object
    def test_query_response_2(self):
        tester = app.test_client(self)
        response = tester.get('/user/query/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Invalid parameter test case
    def test_query_response_3(self):
        tester = app.test_client(self)
        response = tester.get('/user/query/abc')
        statuscode = response.status_code
        self.assertEqual(statuscode, 203)

    # assuming database has at least 1 User object, check whether the return value is json type
    def test_query_content(self):
        tester = app.test_client(self)
        response = tester.get('/user/query/1')
        self.assertEqual(response.content_type, "application/json")

    # Check if content return is application/json
    def test_addUser_content(self):
        tester = app.test_client(self)
        response = tester.post('/user/addUser')
        self.assertEqual(response.content_type, "application/json")
    
if __name__ == "__main__":
    unittest.main()
