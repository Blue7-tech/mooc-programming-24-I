string = input("Please type in a string:")
i = 0
k = -1
while i < len(string):
    print(string[k:])
    k -= 1
    i += 1