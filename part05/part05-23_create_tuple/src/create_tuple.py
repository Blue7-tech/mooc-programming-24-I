# Write your solution here
def create_tuple(x: int, y: int, z: int):
    tuple1 = ()
    list1 = list(tuple1)
    list1.append(x)
    list1.append(y)
    list1.append(z)
    list1.sort()
    sum_of_arguments = sum(list1)
    list1.append(sum_of_arguments)
    list1.pop(1)
    
    tuple1 = tuple(list1) 
    
    return tuple1

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
