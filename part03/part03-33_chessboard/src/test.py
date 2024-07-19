def chessboard(length: int):
    binary_list = [1,0]
    
    iteration_complete = length    
    
    i = 0
    k = 0
    while i < length*length:
        if i == iteration_complete:
            print()
            iteration_complete += length
            if length % 2 == 0:
                k += 1
        print(binary_list[k%2], end = "")
        k += 1
        i += 1
    
if __name__ == "__main__":
    chessboard(6)