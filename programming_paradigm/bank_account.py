class BankAccount:
    def __init__(self , initial_balance= 0 , ):
        
        self.__account_balance = initial_balance
        
        
    def deposit(self, amount) :
        self.__account_balance += amount
            
    def withdraw(self ,amount) :
        if amount < self.__account_balance :
            self.__account_balance -= amount
        else:    
            return False 
          
    def display_balance (self) :
        print(f"Your Current Balance : {self.__account_balance} is low.")      