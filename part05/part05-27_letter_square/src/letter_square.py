# Write your solution here

layers = int(input("Layers:"))

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

width = 1
width_calc = layers

if layers == 1:
    width_calc = 1
else:
    i = 1
    while i < layers:
        width_calc += width
        i += 1

letter_from_temp = ""
temp = []    
for index in range(layers-1,-1,-1):
    print(f"{letter_from_temp}{alphabet[index]*width_calc}{letter_from_temp[::-1]}")
    temp.append(alphabet[index])
    width_calc -= 2
    letter_from_temp = ""
    for item in temp:
        letter_from_temp += item

width_calc = 3
letter_from_temp = ""
temp2 = temp[:layers - 2]
for item in temp2:
    letter_from_temp += item
  
for index in range(1,layers):
    print(f"{letter_from_temp}{alphabet[index]*width_calc}{letter_from_temp[::-1]}")
    if index == layers-1:
        break
    temp2.pop()
    width_calc += 2
    letter_from_temp = ""
    for item in temp2:
        letter_from_temp += item
    