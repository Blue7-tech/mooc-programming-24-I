def line(number: int, characters: str):
    if characters == "":
        print(number*"*")
    else:
        print(number*characters[0])

def box_of_hashes(number: int):
    
    i = 0
    while i < number: 
        line(10, "#")
        i += 1
    
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)