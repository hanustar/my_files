import unittest
from mockExample2 import Gold
class TestSample(unittest.TestCase):

    def test_gold(self):
        obj=Gold()
        response= obj.get()
        self.assertTrue(response.status_code==200)

