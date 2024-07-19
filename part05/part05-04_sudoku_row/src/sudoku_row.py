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

if __name__ == "__main__": 
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 6, 6],
        [3, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    
    print(row_correct(sudoku, 0)) 
    print(row_correct(sudoku, 7))
  