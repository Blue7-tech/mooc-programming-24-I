string = input("Please type in a string:")

if string[1] == string[-2]:
    print(f"The second and the second to last characters are {string[1]}")

if string[1] != string[-2]:
    print(f"The second and the second to last characters are different")