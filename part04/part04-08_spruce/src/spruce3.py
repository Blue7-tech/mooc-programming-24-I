def spruce(number: int):
    print("a spruce!")
    
    white_space = number - 1
    star = "*"
    i = 1
    while i <= number:
        print(f"{white_space*" "}{star}{white_space*" "}")
        star += "**"
        white_space -= 1
        i += 1
    print(f"{" "*(number-1)}*")    
            

if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)