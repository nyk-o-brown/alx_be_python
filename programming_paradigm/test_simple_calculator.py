import unittest


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
class testCase (unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5)
    
    def test_subtraction(self):
        result = 5-2
        self.assertEqual(result, 3)
            
    def  test_multiply(self):
        result =  5*10
        self.assertEqual(result, 10)
    
    def test_divide(self):
        result = 10 /5
        self.assertEqual(result,2)
        
        with self.assertRaises(ValueError):
            self.SimpleCalculator.divide(5, 0)            


if __name__ == '__main__':
    unittest.main()