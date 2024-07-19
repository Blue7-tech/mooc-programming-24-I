def longest_series_of_neighbours(my_list):
    longest = 0
    count = 0
  
    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            if count == 0:
                count += 2
            else:
                count += 1
        elif abs(my_list[i] - my_list[i-1]) != 1:
            count = 0
        if count > 0:
            if count > longest:
                longest = count
    
    return longest        
    
if __name__ == "__main__":
    my_list = [9,8,7,8,7,6,5,4,2,1,6,3,5,7,1,2,3,4,5,6,7,8,9,8,7,1,5,3,1,5]
    print(longest_series_of_neighbours(my_list))