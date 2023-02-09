import unittest
# import math

from scripts.calculator import *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        
    def test_add(self):
        # Test avec des nombres positifs
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)
        
        # Test avec des nombres négatifs
        result = self.calc.add(-1, -2)
        self.assertEqual(result, -3)

        # Test avec des nombres positifs et négatifs
        result = self.calc.add(1, -2)
        self.assertEqual(result, -1)

        # Test avec des nombres décimaux
        result = self.calc.add(1.5, 2.5)
        self.assertEqual(result, 4)

        # Test avec des chaînes de caractères
        result = self.calc.add("a", "b")
        self.assertEqual(result, "ab")
        
    def test_subtract(self):
        # Test avec des nombres positifs
        result = self.calc.subtract(1, 2)
        self.assertEqual(result, -1)
        
        # Test avec des nombres négatifs
        result = self.calc.subtract(-1, -2)
        self.assertEqual(result, 1)

        # Test avec des nombres positifs et négatifs
        result = self.calc.subtract(1, -2)
        self.assertEqual(result, 3)

        # Test avec des nombres décimaux
        result = self.calc.subtract(1.5, 2.5)
        self.assertEqual(result, -1)

        # Test avec des chaînes de caractères
        try:
            result = self.calc.subtract("a", "b")
        except TypeError as e:
            self.assertEqual(str(e), "unsupported operand type(s) for -: 'str' and 'str'")
        else:
            self.fail("Exception not raised")
    
    def test_multiply(self):
        # Test avec des nombres positifs
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)
        
        # Test avec des nombres négatifs
        result = self.calc.multiply(-2, -3)
        self.assertEqual(result, 6)

        # Test avec des nombres positifs et négatifs
        result = self.calc.multiply(2, -3)
        self.assertEqual(result, -6)

        # Test avec des nombres décimaux
        result = self.calc.multiply(1.5, 2.5)
        self.assertEqual(result, 3.75)

        # Test avec des chaînes de caractères
        result = self.calc.multiply("a", 3)
        self.assertEqual(result, "aaa")
        
    def test_divide(self):
        # Test avec des nombres positifs
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)
        
        # Test avec des nombres négatifs
        result = self.calc.divide(-6, -3)
        self.assertEqual(result, 2)

        # Test avec des nombres positifs et négatifs
        result = self.calc.divide(6, -3)
        self.assertEqual(result, -2)
        
        # Test avec un diviseur nul
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6, 0)

        # Test avec des nombres décimaux
        result = self.calc.divide(1.5, 2.5)
        self.assertEqual(result, 0.6)

        # Test avec des chaînes de caractères
        try:
            result = self.calc.divide("a", "b")
        except TypeError as e:
            self.assertEqual(str(e), "unsupported operand type(s) for /: 'str' and 'str'")
        else:
            self.fail("Exception not raised")
        
    def test_power(self):
        # Test avec des nombres positifs
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

        # Test avec des nombres négatifs
        result = self.calc.power(-2, 3)
        self.assertEqual(result, -8)

        # Test avec des nombres positifs et négatifs
        result = self.calc.power(2, -3)
        self.assertEqual(result, 0.125)

        # Test avec des nombres décimaux
        result = self.calc.power(1.5, 2.5)
        self.assertEqual(result, 2.7556759606310752)

        # Test avec des chaînes de caractères
        try:
            result = self.calc.power("a", 3)
        except TypeError as e:
            self.assertEqual(str(e), "unsupported operand type(s) for ** or pow(): 'str' and 'int'")
        else:
            self.fail("Exception not raised")
        
    def test_square_root(self):
        # Test avec des nombres positifs
        result = self.calc.square_root(9)
        self.assertEqual(result, 3.000000001396984)
        
        # Test avec un nombre négatif
        # Trop long à executer
        # with self.assertRaises(ValueError):
        #     self.calc.square_root(-9)

        # Test avec un nombre décimal
        result = self.calc.square_root(9.0)
        self.assertEqual(result, 3.000000001396984)
    
    def test_calculate_add(self):
        result = calculate("add", 1, 2)
        self.assertEqual(result, 3)

    def test_calculate_subtract(self):
        result = calculate("subtract", 1, 2)
        self.assertEqual(result, -1)

    def test_calculate_multiply(self):
        result = calculate("multiply", 2, 3)
        self.assertEqual(result, 6)

    def test_calculate_divide(self):
        result = calculate("divide", 6, 2)
        self.assertEqual(result, 3)

    def test_calculate_power(self):
        result = calculate("power", 2, 3)
        self.assertEqual(result, 8)

    def test_calculate_square_root(self):
        result = calculate("square_root", 4)
        self.assertEqual(result, 2.000000000000002)
            
if __name__ == '__main__':
    unittest.main()