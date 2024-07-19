# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for index in row:
            if index == element:
                count += 1
    return count        
       
if __name__ == "__main__":     
    m = [[5, 6, 3], [2, 6, 1], [6, 6, 6]]
    result = count_matching_elements(m, 1)
    print(result)