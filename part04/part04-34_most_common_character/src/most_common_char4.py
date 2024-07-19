def most_common_character(string):
    occurence = []
    for i in range(len(string)):
        temp = string.count(string[i])
        occurence.append(temp)
        
    most_common = max(occurence)
    index = occurence.index(most_common)
    
    return string[index]
    
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))