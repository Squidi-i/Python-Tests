import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    def test_get_sqrt(self):
        root = get_sqrt(144)
        self.assertEqual(root, 12)
        with self.assertRaises(ValueError):
            get_sqrt(-9)
    
    def test_divide(self):
        quotient = divide(144, 12)
        self.assertEqual(quotient, 12)
        with self.assertRaises(ZeroDivisionError):
            divide(12, 0)
            
    
if __name__ == '__main__':
  unittest.main()