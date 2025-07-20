import random

random_number =random.randint(1,10)

random_number = int(random_number)



guess_number = int(input("can you guess a random number to win a murderd out merc :" ))
match guess_number :
    case _ if guess_number > random_number :
        print(f"Your guess{guess_number} ,was to high ,  \n")
        
    case _ if guess_number < random_number :
        print(f"your guess{guess_number} , was to low , \n")
        
    case _ if guess_number == random_number :
        print(f"your guess{guess_number} ,eas on point ,\n") 
        
    case _ :
        print(f"your guess{guess_number} , was invalid .\n")       
    






