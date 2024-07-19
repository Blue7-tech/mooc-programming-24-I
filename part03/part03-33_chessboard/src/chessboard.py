# Write your solution here
def chessboard(integer):
    i = 1
    while i <= integer:
        if i % 2 != 0:
            k = 1
            sum = ""
            while k <= integer:
                if k % 2 != 0:
                    sum += "1"
                elif k % 2 == 0:
                    sum += "0"
                k += 1
            print(sum)
        elif i % 2 == 0:
            k = 1
            sum = ""
            while k <= integer:
                if k % 2 != 0:
                    sum += "0"
                elif k % 2 == 0:
                    sum += "1"
                k += 1
            print(sum)
        i += 1
# Testing the function
if __name__ == "__main__":
    chessboard(3)
