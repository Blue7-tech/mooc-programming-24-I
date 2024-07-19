def print_sudoku(sudoku: list):
    for row in range(0,9):
        if row == 3 or row ==6:
            print()
        for column in range(0,9):
            if sudoku[row][column] == 0 and column != 3 and column != 6:
                print("_ ", end = "")
            elif sudoku[row][column] != 0 and column != 3 and column != 6:
                print(str(sudoku[row][column])+" ", end = "")
            if sudoku[row][column] == 0 and column == 3:
                print(" _ ", end = "")
            elif sudoku[row][column] != 0 and column == 3:
                print(" " + str(sudoku[row][column]) + " " , end = "")
            if sudoku[row][column] == 0 and column == 6:    
                print(" _ ", end = "")
            elif sudoku[row][column] != 0 and column == 6:
                print(" " + str(sudoku[row][column]) + " ", end = "")
        print()
        
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    
    return sudoku
               
if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
    