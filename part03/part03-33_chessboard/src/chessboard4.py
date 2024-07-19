def chessboard(number: int):
    binary = "10"
    i = 0
    k = 0
    while i < number*number:
        if i % number == 0:
            print()
            if number % 2 == 0:
                k += 1
        print(binary[k % 2], end = "") 
        i+=1
        k+=1


    
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)