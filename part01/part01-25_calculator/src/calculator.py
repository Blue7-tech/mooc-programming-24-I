number1 = int(input("Number1:"))
number2 = int(input("Number2:"))
operation = input("Operation:")

if operation == "multiply":
    print(f"{number1} * {number2} = {number1*number2}")

if operation == "add":
    print(f"{number1} + {number2} = {number1+number2}")

if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
