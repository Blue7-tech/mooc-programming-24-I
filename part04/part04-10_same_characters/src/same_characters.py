# Write your solution here
def same_chars(string, int1, int2):
    x = len(string) - 1
    if int1 > x or int2 > x: 
        return False
    elif string[int1] == string[int2]:
        return True
    elif string[int1] != string[int2]:
        return False
    
    
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("codeer", 3, 10))