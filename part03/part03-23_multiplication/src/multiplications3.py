number = int(input("Please type in a number: "))
number1 = 1
number2 = 1
i = 0
while i < number*number:
    print(f"{number1} x {number2} = {number1*number2}")
    number2 += 1
    if number2 > number:
        number2 = 1
        number1 += 1
    i += 1