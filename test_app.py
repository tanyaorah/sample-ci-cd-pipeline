import unittest
from app import add, divide

class TestApp(unittest.TestCase):
    
    def test_add_positive(self):
        self.assertEqual(add(3, 4), 7)  # Positive test

    def test_add_negative(self):
        self.assertNotEqual(add(3, -4), 0)  # Negative test

    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)  # Positive test

    def test_divide_zero_division(self):
        with self.assertRaises(ValueError):  # Edge case
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
