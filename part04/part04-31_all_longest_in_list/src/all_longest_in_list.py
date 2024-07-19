# Write your solution here

def all_the_longest(my_list):
    longest = []
    longest_len = []
           
    for i in my_list:
        longest_len.append(len(i))
    
    for i in my_list:
        if len(i) == max(longest_len):
            longest.append(i)                       
    return longest
    
    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']