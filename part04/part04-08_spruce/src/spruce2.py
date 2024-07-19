def spruce(number: int):
    print("a spruce!")
    
    white_space = number - 1
    star = "*"
    i = 0
    while i < number+1:
        if i == number:
            white_space = number - 1
            star = "*"
            print(f"{white_space*" "}{star}{white_space*" "}")
            i += 1
        else:
            print(f"{white_space*" "}{star}{white_space*" "}")
            star += "**"
            white_space -= 1
            i += 1
                

if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)