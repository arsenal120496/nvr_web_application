import unittest
from app import app
import random 
import string


class FlaskTest(unittest.TestCase):
    # Test route /camera/getList
    # Check for response 200
    def test_getList_response(self):
        tester = app.test_client(self)
        response = tester.get('/camera/getList')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content return is application/json
    def test_getList_content(self):
        tester = app.test_client(self)
        response = tester.get('/camera/getList')
        self.assertEqual(response.content_type, "application/json")

    # Check for data returned
    def test_getList_data(self):
        tester = app.test_client(self)
        response = tester.get('/camera/getList')
        # check if the return value contains all attribute requirements
        self.assertTrue(b"camera_id" and b"user_id" and b"camera_name" and b"rtsp_url" in response.data)

    # Test route /camera/query/<id>
    def test_query_response_1(self):
        tester = app.test_client(self)
        response = tester.get('/camera/query/0')
        statuscode = response.status_code
        self.assertEqual(statuscode, 203)

    # assuming database has at least 1 Camera object
    def test_query_response_2(self):
        tester = app.test_client(self)
        response = tester.get('/camera/query/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Invalid parameter test case
    def test_query_response_3(self):
        tester = app.test_client(self)
        response = tester.get('/camera/query/abc')
        statuscode = response.status_code
        self.assertEqual(statuscode, 203)

    # assuming database has at least 1 Camera object, check whether the return value is json type
    def test_query_content(self):
        tester = app.test_client(self)
        response = tester.get('/camera/query/1')
        self.assertEqual(response.content_type, "application/json")

    # check if the return value has all required attributes, assuming database has at least 1 Camera object
    def test_query_data(self):
        tester = app.test_client(self)
        response = tester.get('/camera/query/1')
        # check if the return value contains all attribute requirements
        self.assertTrue(b"camera_id" and b"user_id" and b"camera_name" and b"rtsp_url" in response.data)

    # test route /camera/addCamera (check database on DB Browser while testing)
    # test adding a Camera object into the database
    # Expected behavior: should pass first time but might fail second time since Camera object is already
    # added in the database
    def test_addCamera_response_1(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera', json= {
        "user_id": random.randint(1,10e9),
        "camera_name": ''.join(random.choices(string.ascii_lowercase, k=4)),
        "rtsp_url": ''.join(random.choices(string.ascii_lowercase, k=4))
    })
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_addCamera_response_2(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera', json= {
        "user_id": None,
        "camera_name": None,
        "rtsp_url": None})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_addCamera_response_3(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera', json={})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    # missing 1 attribute user_id
    def test_addCamera_response_4(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera', json= {
        "camera_name": "test4",
        "rtsp_url": "test4_url"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    # missing 1 attribute camera_name
    def test_addCamera_response_5(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera', json= {
        "user_id": "5",
        "rtsp_url": "test5_url"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    # missing 1 attirbute rtsp_url
    def test_addCamera_response_6(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera', json= {
        "user_id": "6",
        "camera_name": "test6"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    # Check if content return is application/json
    def test_addCamera_content(self):
        tester = app.test_client(self)
        response = tester.post('/camera/addCamera')
        self.assertEqual(response.content_type, "application/json")
    
if __name__ == "__main__":
    unittest.main()
