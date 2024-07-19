number = int(input("Please type in a number: "))

i = 1

while i < number:
    if i % 2 != 0:
        i += 1
        print(i)
        i -= 1
    elif i % 2 == 0:
        i -= 1
        print(i)
        i += 1
    i += 1


if i % 2 != 0:
    print(i)

elif i % 2 == 0:
    print(i-1)