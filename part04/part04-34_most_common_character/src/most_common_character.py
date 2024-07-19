# Write your solution here

def most_common_character(string):
    list = []
    list2 = ""
    for i in string:
        list.append(string.count(i))
    
    for i in string:
        if string.count(i) == max(list):
            list2 = i
            break
    return list2        


if __name__ == "__main__": 
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))