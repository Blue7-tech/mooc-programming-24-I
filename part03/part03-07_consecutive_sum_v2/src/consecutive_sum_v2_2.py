limit = int(input("Upper limit: "))

temp = "The consecutive sum: 1 + 2"
sum = 1
number = 2       
while sum < limit:
    sum += number
    number += 1
    if sum < limit:
        temp += " + " + str(number)

print(f"{temp} = {sum}")