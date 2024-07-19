number = int(input("Please type in a number:"))

pos_int_value = 2
pos_int_value2 = 1
i = 0
while i < number:      
    if number / 2 == 0:
        if i % 2 == 0:
            print(pos_int_value)
            pos_int_value += 2
        if i % 2 != 0:
            print(pos_int_value2)
            pos_int_value2 += 2
    if number /2 != 0:
        if i % 2 == 0:
            if pos_int_value > number:
                print(number)
                break
            print(pos_int_value)
            pos_int_value += 2
        if i % 2 != 0:
            print(pos_int_value2)
            pos_int_value2 += 2
    i += 1
