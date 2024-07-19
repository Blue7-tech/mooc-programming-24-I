string1 = input("Please type in a string1:")
string2 = input("Please type in a string2:")

if len(string1) > len(string2):
    print(f"{string1} is longer")

elif len(string1) < len(string2):
    print(f"{string2} is longer")

else:
    print("The strings are equally long")

