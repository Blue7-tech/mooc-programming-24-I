# Write your solution here
def invert(dictionary: dict):
    keys = []
    values = []
    i = 0
    
    for key,value in dictionary.items():
        keys.append(key)
        values.append(value)
    
    while i < len(dictionary):
        dictionary[values[i]] = keys[i]
        dictionary.pop(keys[i])
        i += 1
    
    
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
