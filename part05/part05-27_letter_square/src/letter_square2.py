import string

number = int(input("Layers: "))
for_factor = number

factor = {}
k = 1
for i in range(1,27):
    factor[i] = k
    k += 2
    
alphabet = string.ascii_uppercase

temp = ""
for i in range(number-1,-1,-1):
    print(f"{temp}{alphabet[i]*(factor[for_factor])}{temp[::-1]}")
    for_factor -= 1
    temp += alphabet[i]

for_factor = 2
temp = temp[:-2]
for i in range(1,number):
    print(f"{temp}{alphabet[i]*(factor[for_factor])}{temp[::-1]}")
    for_factor += 1
    temp = temp[:-1]