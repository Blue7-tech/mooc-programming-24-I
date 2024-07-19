def spruce(number: int):
    white_space = " "
    fac_white_space = number
    fac_for_star = 1
    print("a spruce!")
    print(f"{white_space*(fac_white_space-1)}{"*"*fac_for_star}")
    
    i = 1
    while i < number:
        fac_white_space -= 1
        fac_for_star += 2
        print(f"{white_space*(fac_white_space-1)}{"*"*fac_for_star}")
        i += 1

    print(f"{white_space*(number-1)}*")

if __name__ == "__main__":
    spruce(12)
