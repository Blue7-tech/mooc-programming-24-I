def chessboard(integer):
    i = 1
    k = 1
    j = 1
    while i <= integer:
        sum = ""
        while k <= integer:
            if j % 2 != 0:
                sum += "1"
            elif j % 2 == 0:
                sum += "0"
            j += 1
            k += 1
        print(sum)
        if integer % 2 == 0:
            j += 1
        k = 1
        i += 1
# Testing the function
if __name__ == "__main__":
    chessboard(99)
