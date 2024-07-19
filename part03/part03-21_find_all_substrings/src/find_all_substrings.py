string = input("Please type in a word:")
character = input("Please type in a character:")
i = 0

while i < len(string)-2:
    if string[i] == character:
        print(string[i:i+3])
    i += 1



