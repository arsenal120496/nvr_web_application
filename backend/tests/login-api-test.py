import unittest
import sys
sys.path.insert(1,'C:\\Users\\vinhh\\Desktop\\nvr_web_application\\backend')
from service.user import *
class FlaskTest(unittest.TestCase):
    def test_get_database(self):
        result = get_database()
        expected_result = []
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
