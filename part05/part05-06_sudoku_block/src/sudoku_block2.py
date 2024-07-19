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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))