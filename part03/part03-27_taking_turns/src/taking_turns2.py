number = int(input("Please type in a number:"))

i = 0
index_start = 1
index_end = number
while i < number:
    if number % 2 == 0:
        print(index_start)
        print(index_end)
        index_start += 1
        index_end -= 1
        i += 2
    if number % 2 != 0:
        if index_start == index_end:
            print(index_start)
            break
        print(index_start)
        print(index_end)
        index_start += 1
        index_end -= 1
        i += 2