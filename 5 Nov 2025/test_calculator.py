import unittest
from calculator import calculator_area

class TestAreaFunction(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(calculator_area(2,3),6)
    
    def test_raiseError(self):
        with self.assertRaises(ValueError):
            calculator_area(-10,8)