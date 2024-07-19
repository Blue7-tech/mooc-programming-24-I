def line(number: int, characters: str):
    if characters == "":
        print(number*"*")
    else:
        print(number*characters[0])

def triangle(number: int):
    i = 0
    k = 1
    while i < number:
        line(k, "#")
        i += 1
        k += 1
    
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)