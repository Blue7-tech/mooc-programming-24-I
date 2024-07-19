def row_correct(sudoku: list, row_no: int):
    occurence = []
    
    for i in range(1, 10):
        occurence.append(sudoku[row_no].count(i))
    if max(occurence) > 1:  
        return False
    else:
        return True
        

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        if row[column_no] != 0 and row[column_no] in column:
            return False
        column.append(row[column_no])
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    
    for i in range(3):
        temp = []
        temp.append(sudoku[row_no][column_no])
        temp.append(sudoku[row_no][column_no+1])
        temp.append(sudoku[row_no][column_no+2])
        row_no += 1
        block.append(temp)
    
    checked = []
    for row in block:
        for number in row:
            if number != 0 and number in checked:
                return False
            checked.append(number)
            
    return True 

def sudoku_grid_correct(sudoku: list):
    k = 0
    l = 0
    for i in range(9):
        if i == 3:
            l = 0
            k += 3
        if i == 6:
            l = 0
            k += 3
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
        if not block_correct(sudoku, k, l):
            return False
        l += 3

    return True
    
if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))