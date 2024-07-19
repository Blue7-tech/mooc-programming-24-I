def most_common_character(characters):
    
    result = []
    for char in characters:
        temp_list = []
        temp = characters.count(char)
        temp_list.append(temp)
        temp_list.append(char)
        result.append(temp_list)
    print(result)
    
    temp = 0
    for item in result:
        if item[0] > temp:
            temp = item[0]        

    final = ""
    for item in result:
        if item[0] == temp:
            final += item[1] 
            break
    return final

if __name__ == "__main__":
    first_string = "exemplaryelementary"
    print(most_common_character(first_string))