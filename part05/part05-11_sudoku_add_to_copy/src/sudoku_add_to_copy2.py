def print_sudoku(sudoku: list):
        
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row][column] == 0:
                sudoku[row][column] = "_"    
    
    for row in range(0,9):
        if row == 3 or row == 6:
            print()
        for column in range(0,9):
            if column == 2 or column == 5:
                print(str(sudoku[row][column]) + "  ", end = "")
                continue
            if column == 8:
                print(str(sudoku[row][column]), end = "")
                continue
            print(str(sudoku[row][column]) + " ", end = "")
        print()        

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = []
    copy = sudoku[:][:]
    copy[row_no][column_no] = number
    return copy
    
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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)