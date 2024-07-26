#CALCULATOR
def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the number corresponding to the operation: ")
    # Perform the operation
    if operation == '1' or operation == '+':
        result = num1 + num2
        operation_symbol = "+"
    elif operation == '2' or operation == '-':
        result = num1 - num2
        operation_symbol = "-"
    elif operation == '3' or operation == '*':
        result = num1 * num2
        operation_symbol = "*"
    elif operation == '4' or operation == '/':
        if num2 != 0:
            result = num1 / num2
            operation_symbol = "/"
        else:
            print("Error")
            return
    else:
        print("Invalid operation.")
        return
    # Display the result
    print(f"{num1} {operation_symbol} {num2} = {result}")
calculator()
