def line(number: int, characters: str):
    if characters == "":
        print(number*"*")
    else:
        print(number*characters[0])

def square(number: int, characters: str):
    i = 0
    while i < number:
        line(number, characters)
        i += 1
    
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")