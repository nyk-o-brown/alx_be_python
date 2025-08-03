
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

