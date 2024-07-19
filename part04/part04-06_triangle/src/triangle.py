# Copy here code of line function from previous exercise

def line(size, character):

    if character == "":

        character = "*"

    print(character[0] * size)
    

def triangle(star):
    # You should call function line here with proper parameters
    
    size = 1
    while size <= star:
        line(size, "#")
        size += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
