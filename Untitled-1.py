number1 = float(input("First number: "))
number2 = float(input("Second number: "))

operation = input("Operation (+, -, *, /): ")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero" 
else:    result = "Error: Invalid operation"
print("Result:", result)