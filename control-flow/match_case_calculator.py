num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /): ")
#def opertaion(value):
match operation:
        case '-':
           result = num1 - num2
           print(f"The result is {result}")
        case '+':
            result = num1 + num2
            print(f"The result is {result}")
        case '*':
           result = num1 * num2
           print(f"The result is {result}")
        case '/':
            if num2 != 0:
               result = num1 / num2
               print(f"The result is {result}")
            else:
                print( "Error: Cannot divide by zero")
        case '_':
           result = "Invalid operation selected."
