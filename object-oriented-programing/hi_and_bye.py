class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def greet(self):
        print(f"hello{self.name} in {self.age}")    
    
    def __del__(self):
        return f"goodbye {self.name}"
    

if __name__ == "__main__":
    
    person1 =person("magere" ,33)
    
    person1.greet()    
    