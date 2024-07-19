string = input("Please type in a word:")
length = len(string)
character = input("Please type in a character:")

if length > 2:
    index = string.find(character)
    if index < length - 2:
        print(string[index:index+3])


