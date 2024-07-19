number_1 = int(input("Please type in the first number:"))
number_2 = int(input("Please type in another number:"))

if number_1 > number_2:
    print(f"The greater number was {number_1}")

if number_2 > number_1:
    print(f"The greater number was {number_2}")

if number_2 == number_1:
    print("The numbers are equal!")