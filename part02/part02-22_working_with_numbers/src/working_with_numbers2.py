print("Please type in integer numbers. Type in 0 to finish.")

count_number = 0
count = ""
pos = ""
neg = ""
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    if number > 0:
        pos += "i"
    elif number < 0:
        neg += "i"
    count += "i"
    count_number += number


print(f"""
...the program asks for numbers
numbers typed in {len(count)}
The sum of the numbers is {count_number}
The mean of the numbers is {count_number/len(count)}
Positive numbers {len(pos)}
Negative numbers {len(neg)}
""")