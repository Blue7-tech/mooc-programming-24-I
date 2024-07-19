# Write your solution here

def list_of_stars(test):
    for x in test:
        a = x * "*"
        print(a)
    
    
if __name__ == "__main__":
    my_list = [3,7,1,1,2]
    list_of_stars(my_list)