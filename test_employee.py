import unittest
import requests
from mockExample2 import Gold
from unittest.mock import patch
from Employee import Employee
class Test_Employee(unittest.TestCase):
    def setUp(self):
        self.emp_1= Employee("hanu","star","10000")
    def tearDown(self):
        pass
    def test_email(self):
        self.assertEqual(self.emp_1.email(),"hanu.star@gmail.com")
    def test_fulName(self):
        result= self.emp_1.fullName()
        self.assertTrue(result=="hanu star")
        print(self.emp_1.fullName())
    def test_pay(self):
        self.emp_1.pay()
        self.assertEqual(self.emp_1.pay(), 20000)



if __name__ == '__main__':
    unittest.main()
