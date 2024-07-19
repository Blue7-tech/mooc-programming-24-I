def longest_series_of_neighbours(my_list):
    
    temp = 0
    longest = 0
    count = 1
    prev_index = 0 
    i = 1
    while i < len(my_list):
        if abs(my_list[i]-my_list[prev_index]) == 1:
            count += 1
        elif abs(my_list[i]-my_list[prev_index]) != 1:
            if count != 0 and count > temp:
                temp = count
            count = 0
            count += 1
        if count >= temp:
            longest = count 
        i += 1
        prev_index += 1    

    return longest

if __name__ == "__main__":
    my_list = [9,8,7,8,7,6,5,4,2,1,6,3,5,7,1,2,3,4,5,6,7,8,9,8,7,1,5,3,1,5]
    print(longest_series_of_neighbours(my_list))