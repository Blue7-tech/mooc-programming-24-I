string = input("Please type in a string: ")
sub = input("Please type in a substring: ")

index = 0
i = 0
while i < 2:
    index = string.find(sub, index)
    if i == 1:
        if index == -1:
            print("The substring does not occur twice in the string.")
            break
        break
    index += 1
    i += 1

if index != -1:
    print(f"The second occurrence of the substring is at index {index}.")