# Write your solution here

"""def oldest_person(people: list):
    dictionary = {}
    values = []
    for x in people:
        dictionary[x[0]] = x[1]

    for value in dictionary.values():
        values.append(value)
    
    tuple_values = tuple(values)
    oldest = min(tuple_values)
    
    for key,value in dictionary.items():
        if value == oldest:
            return key"""

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))