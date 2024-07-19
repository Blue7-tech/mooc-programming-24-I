
def play_turn(game_board: list, x: int, y: int, piece: str):
    if not 0 <= x < 3 or not 0 <= y < 3:
        return False

    if piece == "X" or piece == "O":
        pass
    else:
        return False
    
    if game_board[y][x] == '':
        game_board[y][x] = piece
        return True
    else:
        return False
    
if __name__ == "__main__":
    game_board = [['', '', 'O'], ['', '', ''], ['X', '', 'O']]
    print(play_turn(game_board, 0, 0, "A"))
    print(game_board)