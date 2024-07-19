def no_vowels(characters):
    vowels = "aeoui"
    result = ""
    for char in characters:
        if char in vowels:
            continue
        result += char
    return result
    
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))