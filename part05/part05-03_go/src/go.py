# Write your solution here

def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for item in row:
            if item == 1:
                player1 += 1
            if item == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
    
if __name__ == "__main__":     
    m = [
        [0, 2, 2, 0, 2, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 1, 1, 1, 0],
        [0, 2, 2, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 1, 0, 2, 0, 0]
    ]
    value = who_won(m)
    print(value)   
