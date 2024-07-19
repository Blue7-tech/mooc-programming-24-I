# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
    
def shape(size1, character1, size2, character2):
    i = 1
    while i <= size1:
        line(i, character1)
        i += 1
    
    while size2 > 0:
        line(size1, character2)
        size2 -= 1

if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")