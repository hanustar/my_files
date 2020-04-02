import unittest

class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5,9)
    def test2(self):
        self.assertNotEqual(5 * 2,11)
    def test3(self):
        self.assertTrue(4 + 5 == 9,"The result is False")
    def test4(self):
        self.assertFalse(4 + 5 == 10,"assertion fails")
    def test5(self):
        self.assertIn(3,[1,2,3])
    def test6(self):
        self.assertNotIn(5, range(5))

if __name__ == '__main__':
    unittest.main()