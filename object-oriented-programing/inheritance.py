class animals:
    
    def eat(self):
        print("I am hungry")
        
    
    def sleep(self):
        print("I am sleeping")    
    
class Dog(animals):
        def bark(self):
            print("The dog is barking")
        

if __name__ =="__main__":
    
    animal1 = animals()
    animal1.eat()
    animal1.sleep()
    
    dog1 = Dog()
    
    dog1.eat()
    dog1.bark()
                