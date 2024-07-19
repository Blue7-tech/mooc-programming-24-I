# write your solution here

def row_sums():
    with open("matrix.txt") as file:
        row_sums = []
        for line in file:
            parts = line.split(",")
            a = 0
            for number in parts:
                if int(number) != 0:
                    a += int(number)
            
            row_sums.append(a)
        return row_sums
        
def matrix_sum():
    with open("matrix.txt") as file:
        row_sums = []
        for line in file:
            parts = line.split(",")
            a = 0
            for number in parts:
                if int(number) != 0:
                    a += int(number)
            row_sums.append(a)
        a = 0
        for sum in row_sums:
            a += sum
        return a
    
def matrix_max():
    with open("matrix.txt") as file:
        row_sums = []
        for line in file:
            parts = line.split(",")
            a = 0
            start = True
            for number in parts:
                if start or int(number) > a:
                    a = int(number)
                    start = False
            row_sums.append(a)
        
        a = 0
        for sum in row_sums:
            if sum > a:
                a = sum
        
        return a
        

if __name__ == "__main__":            
    print(matrix_max())
    print(matrix_sum())
    print(row_sums())  
        
        


           
            
            
       