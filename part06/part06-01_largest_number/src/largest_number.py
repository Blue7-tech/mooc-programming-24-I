# write your solution here
def largest():
    with open("numbers.txt") as file:
        a = 0
        for number in file:
            if int(number) > a:
                a = int(number)
            return a
if __name__ == "__main__":        
    print(largest())
    
