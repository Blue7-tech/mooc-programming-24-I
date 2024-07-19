print("Please type in integer numbers. Type in 0 to finish.")

i = 0
sum = 0
mean = 0
k = 0
l = 0

while True:
    number = int(input("Number:"))
    i += 1
    sum += number
    mean = sum / i

    if number > 0:
        k += 1

    if number < 0:
        l += 1

    if number == 0:
        i -= 1
        sum -= number
        mean = sum / i
        print(f"Numbers typed in {i}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {mean}")
        print(f"Positive numbers {k}")
        print(f"Negative numbers {l}")
        break