def who_won(game_board: list):
    player1 = 0
    player2 = 0
    
    for row in game_board:
        if row.count(1) > 0:
            player1 += row.count(1)
        if row.count(2) > 0:
            player2 += row.count(2)
    
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
        
            
if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 1, 0, 0, 2, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 2, 0],
        [0, 1, 0, 0, 0, 2, 0, 2, 0],
        [0, 1, 0, 2, 0, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    print(who_won(sudoku))    