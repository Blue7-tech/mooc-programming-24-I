# write your solution here
def read_fruits():
    dictionary = {}
    with open("fruits.csv") as file:
        for fruit in file:
            parts = fruit.split(";")
            float(parts[1])
            dictionary[parts[0]] = float(parts[1])
    
    return dictionary
if __name__ == "__main__":    
    print(read_fruits())

    