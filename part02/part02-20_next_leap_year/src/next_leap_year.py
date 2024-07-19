to_test = int(input("Please type in a year: "))
temp = to_test
while True:
    temp += 1
    if temp % 100 != 0 and temp % 4 == 0: 
        break
    elif temp % 100 == 0 and temp % 400 == 0: 
        break
print(f"The next leap year after {to_test} is {temp}")
