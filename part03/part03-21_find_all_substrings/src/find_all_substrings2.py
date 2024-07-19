string = input("Find the first substring: ")
character = input("Please type in a character: ")

i = 0
index = 0
while i <= string.count(character):
    if character in string:
        index = string.find(character, index)
        if len(string)-1 - index >= 2:
            print(string[index:index+3])
    else:
        pass
    index += 1
    i += 1