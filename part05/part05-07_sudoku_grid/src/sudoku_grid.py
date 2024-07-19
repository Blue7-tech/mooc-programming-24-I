# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    correct = []
    
    for number in row:
        if number > 0:
            correct.append(number)
    
    a = []
    for number in correct:
        if number in a:
            return False                
        else:
            a.append(number)
    return True              

def column_correct(sudoku: list, column_no: int):
    
    correct = []
    
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in correct:
            return False
        correct.append(row[column_no])
    return True           

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = [] 
    i = 0
    for row in range(row_no, row_no + 3):
        block.append(sudoku[row_no + i][column_no:column_no + 3])
        i += 1        
   
    block1 = []
    for row in block:
        for number in row:
            if number > 0 and number in block1:
                return False
            block1.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    i = 0
    while i <= 8:
        row_correct(sudoku,i)
        if row_correct(sudoku,i) == False:
            return False
        column_correct(sudoku,i)
        if column_correct(sudoku,i) == False:
            return False
        i += 1
    
    i = 0
    j= 0
    while i < 3:
        block_correct(sudoku,0,j)
        if block_correct(sudoku,0,j) == False:
            return False
        j += 3
        i += 1
    
    i = 0
    j= 0
    while i < 3:
        block_correct(sudoku,3,j)
        if block_correct(sudoku,3,j) == False:
            return False
        j += 3
        i += 1
    
    i = 0
    j= 0    
    while i < 3:
        block_correct(sudoku,6,j)
        if block_correct(sudoku,6,j) == False:
            return False
        j += 3
        i += 1
    
    return True
     
if __name__ == "__main__": 
    sudoku = [
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
    
    print(sudoku_grid_correct(sudoku))
    
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