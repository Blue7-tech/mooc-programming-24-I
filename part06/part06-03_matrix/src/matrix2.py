def get_numbers():
    numbers = []
    with open("matrix.txt") as file:
        for line in file:
            parts = line.split(",")
            for part in parts:
                numbers.append(int(part))
    
    return numbers
    
def matrix_sum():
    numbers = get_numbers()           
    return sum(numbers)

def matrix_max():
    numbers = get_numbers()          
    return max(numbers)

def row_sums():
    sums = []
    
    with open("matrix.txt") as file:
        for line in file:
            line.strip()
            parts = line.split(",")
            parts_int = []
            for part in parts:
                parts_int.append(int(part))
            sums.append(sum(parts_int))
 
            
    return sums

print(matrix_sum())
print(matrix_max())
print(row_sums())