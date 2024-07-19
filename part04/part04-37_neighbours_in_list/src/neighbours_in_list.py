# Write your solution here
def longest_series_of_neighbours(my_list: list):
    longest_list = []
    temp_list = []
    start = 0
    temp = 0

    for i in range(len(my_list)):
        if start == 0:
            temp += my_list[i]
            if i + 1 < len(my_list)-1 and i != 0:
                if temp - my_list[i-1] == 1 or temp - my_list[i-1] == -1:
                    temp_list.append(my_list[i-1])
                    temp_list.append(temp)
                elif temp - my_list[i+1] == 1 or temp - my_list[i+1] == -1:
                    temp_list.append(temp)
            elif i == 0:
                if temp - my_list[i+1] == 1 or temp - my_list[i+1] == -1:
                    temp_list.append(temp)
            else:
                if temp - my_list[i-1] == 1 or temp - my_list[i-1] == -1:
                    temp_list.append(my_list[i-1])
                    temp_list.append(temp)               
            start += 1
        elif my_list[i] - temp == 1 or my_list[i] - temp == -1:
            temp_list.append(my_list[i])
            temp = my_list[i]
        else:
            longest_list.append(temp_list)
            temp_list=[]
            temp = 0
            start = 0
 
    if len(temp_list) != 0:
        longest_list.append(temp_list)  
    
    temp = 0
    for i in longest_list:
        if len(i) > temp:
            temp=len(i)

    return temp

   
if __name__ == "__main__":
    my_list = [9,8,7,8,7,6,5,4,2,1,6,3,5,7,1,2,3,4,5,6,7,8,9,8,7,1,5,3,1,5]
    print(longest_series_of_neighbours(my_list))
