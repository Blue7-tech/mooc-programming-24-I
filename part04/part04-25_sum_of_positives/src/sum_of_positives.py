# Write your solution here

def sum_of_positives(my_list):
    list=[]
    for x in my_list:
        if x < 0:
            continue
        list.append(x)
    return sum(list)
    
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)