# Write your solution here

def shortest(my_list):
    shortest = my_list[0]
    for i in my_list:
        if len(i) < len(shortest):
            shortest = i
    return shortest
    
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)