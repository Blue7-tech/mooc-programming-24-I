

while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        break
    i = 0
    k = 1
    l = 1
    while True:
        if i == number:
            break
        k *= l
        l += 1
        i += 1
    print(f"The factorial of the number {number} is {k}")    