def line(number: int, characters: str):
    if characters == "":
        print(number*"*")
    else:
        print(number*characters[0])
        
def shape(number1: int, characters1: str, number2: int, characters2: str):
    i = 0
    k = 1
    while i < number1:
        line(k, characters1)
        i += 1
        k += 1
    
    i = 0
    while i < number2:
        line(number1, characters2)
        i += 1
    
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")