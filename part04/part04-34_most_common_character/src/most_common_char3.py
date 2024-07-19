def most_common_character(characters): 
    occurence = []
    
    for char in characters:
        occurence.append(characters.count(char))

    for char in characters:
        if characters.count(char) == max(occurence):
            return char
    
if __name__ == "__main__":
    first_string = "exemplaryelementary"
    print(most_common_character(first_string))
