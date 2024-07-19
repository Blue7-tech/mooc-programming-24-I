def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            temp = line.split(";")
            fruits[temp[0]] = float(temp[1])
    
    return fruits

print(read_fruits())