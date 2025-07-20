

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    answer = num1 + num2
    print(f"The result is {answer}")
elif operation == "-":
    answer = num1 - num2
    print(f"The result is {answer}")
elif operation == "*":
    answer = num1 * num2
    print(f"The result is {answer}")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        answer = num1 / num2
        print(f"The result is {int(answer)}")
else:
    print("Invalid operation selected.")
