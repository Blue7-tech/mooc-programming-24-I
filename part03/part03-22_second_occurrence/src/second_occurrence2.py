string = input("Please type in a string: ")
sub_string = input("Please type in a substring: ")


if sub_string in string:
    index = 0
    i = 0
    while i < 2:
        index = string.find(sub_string, index)
        if i == 1 and index != -1:
            print(f"The second occurence of the substring is at index {index}")
        if i == 1 and index == -1:
            print("The substring does not occur twice in the string.")
        index += 1
        i += 1

else:  
    print("The substring does not occur twice in the string.")
    