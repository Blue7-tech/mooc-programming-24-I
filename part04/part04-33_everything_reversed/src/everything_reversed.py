# Write your solution here

def everything_reversed(my_list):
    list = my_list[::-1]
    list2 = []
    for i in list:
        list2.append(i[::-1])
        
    return list2

if __name__ == "__main__": 
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

    