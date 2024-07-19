string = input("Please type in a string:")
length = len(string)
print(string[length-1])
i = -2

while i >= (len(string) * -1):
    print(string[length+i:])
    i -= 1