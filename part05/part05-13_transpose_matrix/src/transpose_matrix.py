# Write your solution here
def transpose(matrix: list):
    length = len(matrix)
    b = []
    for i in range(length):
        for j in range (length):
            b.append(matrix[j][i])
            
    matrix.insert(0,b)
    
    for i in range(length):
        matrix.pop(1)
        
    b = length    
    for i in range(length-1):
        matrix.append(matrix[0][b:b+length])
        b+=length
           
    matrix[0] = matrix[0][0:length]

if __name__ == "__main__":       
    matrix=[
        [2, 3, 4, 5],
        [6, 7, 8, 9],
        [9, 8, 7, 6],
        [5, 4, 3, 2]
        ]
    print(transpose(matrix))
    
  



    
    
    
    
    