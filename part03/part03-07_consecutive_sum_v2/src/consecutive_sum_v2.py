upper_limit = int(input("Upper limit:"))
number = 0
sum = 0
string = ""

while sum < upper_limit:
    number += 1
    sum += number
    string += str(number) + " " "+" " "

print(f"The consecutive sum: {string[:-2]} =  {sum}")