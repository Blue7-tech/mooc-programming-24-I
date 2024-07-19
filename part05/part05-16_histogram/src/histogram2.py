def histogram(characters:str):
    
    dict_histo = {}
    for char in characters:
        if char in dict_histo:
            continue
        dict_histo[char] = characters.count(char)
    
    for key, value in dict_histo.items():
        print(f"{key} {value*"*"}")
    
if __name__ == "__main__":
    histogram("statistically")