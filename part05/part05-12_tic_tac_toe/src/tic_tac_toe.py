# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= x <=2 and 0 <= y <=2:       
        
        game_board2 = []
        i = 0
        for row in game_board:
            if i == y and row[x] != "":
                return False
            if i == y and row[x] == "":
                row[x] = piece 
                game_board2.append(row[:])
                i += 1
                continue
            game_board2.append(row[:])
            i += 1  
        
        return True      
    
    else:
        return False      

if __name__ == "__main__":
    game_board = [
    ["", "", "X"], 
    ["X", "X", ""], 
    ["", "O", ""]
    ]
    print(play_turn(game_board, 0, 1, "O"))
    print(game_board)
    