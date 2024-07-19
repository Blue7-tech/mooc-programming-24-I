def chessboard(count: int):
    
    i = 0
    while i < count:
        if i % 2 == 0:
            char = "10"
            to_add = count - len(char)
            for k in range(to_add):
                char += char[k%len(char)]
            print(char)
        if i % 2 != 0:
            char = "01"
            to_add = count - len(char)
            for k in range(to_add):
                char += char[k%len(char)]
            print(char)
        i += 1

chessboard(3)
print()
chessboard(6)