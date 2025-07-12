#define two numbers to perform operations
number1= 10
number2= 5

number1 = 10 
number2 = 5

#perform basic arithmetis operations
Addition= number1 + number2
Subtraction= number1 - number2
Multiplication= number1 * number2

#Ask the user which operation they would like to perform
print("would you like to perform -Addition-, -Subtraction-, -Multiplication-,")

#Get the users input
Operation = input("Enter the operation :")

#display the data accordint to the users option
if Operation == "Addition":
    print(f"Sum of {number1} and {number2} is {Addition}")

if Operation == "Subtraction":
    print(f"Subtraction of {number1} and {number2} is {Subtraction}")
    
if Operation == "Multiplication":
    print(f"Multiplication of {number1} and {number2} is {Multiplication}")        