string = input("Please type in a string:")
second = string[1]
second_to_last = string[-2]

if second != second_to_last:
    print("The second and the second to last characters are different")

else:
    print(f"The second and the second to last characters are {string[1]}")