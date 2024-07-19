def transpose(matrix: list):
    start = 0
    for i in range(len(matrix)):
        for j in range(start, len(matrix)):
            if i == j:
                continue
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            start += 1
    
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transpose(matrix)
    print(matrix)