def everything_reversed(my_list):
    result = []
    for i in range(len(my_list)-1, -1, -1):
        string = my_list[i]
        result.append(string[::-1])
    
    return result

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)