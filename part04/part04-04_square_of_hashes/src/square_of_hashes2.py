def line(number: int, characters: str):
    if characters == "":
        print(number*"*")
    else:
        print(number*characters[0])

def square_of_hashes(number: int):
    i = 0 
    while i < number:
        line(number, "#")
        i += 1
    
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)