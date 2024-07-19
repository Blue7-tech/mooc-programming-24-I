number = int(input("Please type in a number:"))

i = 1
k = 1

while i <= number:
    a = i * k
    print(f"{i} x {k} = {a}")
    while k < number:
        k += 1
        a = i * k
        print(f"{i} x {k} = {a}")
    else:
        k = 1
    i += 1

