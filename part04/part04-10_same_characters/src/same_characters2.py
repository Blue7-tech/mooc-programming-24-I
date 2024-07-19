def same_chars(characters: str, index1: int, index2: int):
 
    if index1 > len(characters)-1 or index2 > len(characters)-1:
        return False
    
    if characters[index1] == characters[index2]:
        return True
    else:
        return False

if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False