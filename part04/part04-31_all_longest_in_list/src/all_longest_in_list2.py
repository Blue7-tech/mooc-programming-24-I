def all_the_longest(my_list):
    result = []
    longest_string = ""
    temp = len(my_list[0])
    for string in my_list:
        if len(string) > temp:
            longest_string = string
    result.append(longest_string)
    return result
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']