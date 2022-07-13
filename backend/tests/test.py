from app import app
import unittest
class FlaskTest(unittest.TestCase):
    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        assert response.status_code == 200

if __name__ == "__main__":
    unittest.main()
