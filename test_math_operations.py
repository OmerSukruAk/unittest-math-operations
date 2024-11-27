import unittest 
from math_operations import Math_Operations

class TestMathOperations(unittest.TestCase):

    @classmethod
    def setUpClass(self): # Difference between setUp is intended to run before each test method instead using @classmethod should be used with setUpClass which runs once for the entire class before any tests are executed.
        self.math_operations = Math_Operations()
    
    def test_add_positive_numbers(self):
        self.assertEqual(self.math_operations.add(1, 2), 3)
        self.assertEqual(self.math_operations.add(-2, -3), -5)
        with self.assertRaises(ValueError):
            self.math_operations.mul(True, 0)
        with self.assertRaises(ValueError):
            self.math_operations.mul("omer",5)
    
    def test_subtract_numbers(self):
        self.assertEqual(self.math_operations.sub(9, 8),1)
        self.assertEqual(self.math_operations.sub(-5, -5), 0)
        with self.assertRaises(ValueError):
            self.math_operations.mul(True, 0)
        with self.assertRaises(ValueError):
            self.math_operations.mul("omer",5)
    
    def test_multiply_numbers(self):
        self.assertEqual(self.math_operations.mul(5, 10), 50)
        self.assertEqual(self.math_operations.mul(-5, -10), 50)
        self.assertEqual(self.math_operations.mul(0,4),0)
        with self.assertRaises(ValueError):
            self.math_operations.mul(True, 0)
        with self.assertRaises(ValueError):
            self.math_operations.mul("omer",5)
    
    def test_divide_numbers(self):
        self.assertEqual(self.math_operations.div(10,2),5)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.math_operations.div(10,0))
        with self.assertRaises(ValueError):
            self.math_operations.mul(True, 0)
        with self.assertRaises(ValueError):
            self.math_operations.mul("omer",5)
