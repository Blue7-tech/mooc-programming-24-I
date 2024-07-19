def largest():
    with open("numbers.txt") as file:
        largest = 0
        for line in file:
            to_test = int(line.strip())
            if to_test > largest:
                largest = to_test
    
    return largest

print(largest())