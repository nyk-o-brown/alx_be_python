import unittest
import calc



class SimpleCalculator():
    
    def add(self , a, b):
        result = a+b
        return result
    
    def subtract (self , a, b):
        result = a-b
        return result
    
    def multiply (self, a, b):
        result = a*b
        return result
    
    def divide (self, a, b):
        if b==0:
            return None
        result = a/b
        return result




from simple_calculator import SimpleCalculator
class testCalc(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
            
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)           


if __name__ == '__main__':
    unittest.main()