string = input("Find the first substring: ")
character = input("Please type in a character: ")

if character in string:
    index = string.find(character)
    if len(string)-1 - index >= 2:
        print(string[index:index+3])

else:
    pass
    