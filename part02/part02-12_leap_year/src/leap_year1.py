to_test = int(input("Please type in a year: "))

if to_test % 100 == 0:
    if to_test % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")

elif to_test % 100 != 0:
    if to_test % 4 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
        