# Write your solution here
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
    
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    
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