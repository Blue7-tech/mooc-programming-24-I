
# Write your solution here
from string import punctuation

def change_case(orig_string: str):
    return orig_string.swapcase()
    
def split_in_half(orig_string: str):
    
    if len(orig_string) % 2 == 0:
        split_in_half_tuple = (orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:])
    elif len(orig_string) % 2 != 0:
        split_in_half_tuple = (orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:])
    
    return split_in_half_tuple
    
def remove_special_characters(orig_string: str):
    
    string_punctuation = punctuation + "§" + "¤"
    
    to_remove = []
    for char in orig_string:
        if char in string_punctuation and char not in to_remove:
            to_remove.append(char)
    
    string_wo = orig_string
    for char in to_remove:
        string_wo = string_wo.replace(char, "")
                
    
    return string_wo

if __name__ == "__main__":
    print(change_case("AbgasFlaschen"))
    print(split_in_half("Well hello there!"))
    print(remove_special_characters("We###ll he!ll???o there!????"))