number = int(input("Please type in a number: "))
number2 = 1
a = False
if number % 2 != 0:
    a = True

while True: 
    if number == number2:
        break
    print(number2)
    print(number)
    number2 += 1
    number -= 1
    if number <= number2:
        break
       
if a:
    print(number2)
