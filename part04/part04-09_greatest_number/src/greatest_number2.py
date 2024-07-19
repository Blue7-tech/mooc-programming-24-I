def greatest_number(numb1, numb2, numb3):
    if numb1 > numb2 and numb3:
        return numb1
    
    elif numb2>numb3:
        return numb2
    
    else:
        return numb3

if __name__ == "__main__":
    print(greatest_number(5, 4, 1)) # 4
    print(greatest_number(99, -4, 7)) # 99
    print(greatest_number(0, 0, 0)) # 0