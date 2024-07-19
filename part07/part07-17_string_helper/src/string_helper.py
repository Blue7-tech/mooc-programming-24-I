import string
def change_case(orig_string: str):
    mod_string = orig_string.swapcase()
    return mod_string
    
def split_in_half(orig_string: str):
    if len(orig_string) % 2 == 0:
        return orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:]
    else:
        return orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:]
    
def remove_special_characters(orig_string: str):
    specials = string.punctuation + "§" + "¤"
    mod_string = ""
    for char in orig_string:
        if char in specials:
            continue
        else:
            mod_string += char
    return mod_string