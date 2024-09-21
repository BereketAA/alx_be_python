num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /): ")
#def opertaion(value):
match operation:
        case '-':
            result = f"The answer is = {num1 - num2}"
        case '+':
            result = f"The answer is = {num1 + num2}"
        case '*':
           result = f"The answer is = {num1 * num2}"
        case '/':
            if num2 != 0:
               result = f"The answer is = {num1 / num2}"
            else:
                print( "Error: Cannot divide by zero")
        case '_':
           result = "Invalid operation selected."
print(result)