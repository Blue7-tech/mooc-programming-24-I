import string

def separate_characters(my_string: str):
    letters = string.ascii_letters
    punctuation = string.punctuation
    parts = ["", "", ""]
    
    for char in my_string:
        if char in letters:
            parts[0] += char
        elif char in punctuation:
            parts[1] += char
        else:
            parts[2] += char
    
    return parts
    
if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])