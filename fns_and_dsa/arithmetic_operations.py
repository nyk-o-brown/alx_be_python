def perform_operation(num1, num2, operation):
    """Performs arithmetic operations and handles division by zero."""

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is undefined"
        return num1 / num2

    else:
        return "Error: Invalid operation"
