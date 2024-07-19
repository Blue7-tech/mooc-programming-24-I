# Write your solution here
# You can test your function by calling it within the following block
    
def spruce(size):
    print("a spruce!")
    char = (size + size - 1) * "*"
    print(" " * (size-1) + char[size-1])     
    i = 1
    k = 2
    while i <= size-1:
        print(" " * (size-k) + char[size-k:size+i])
        k += 1  
        i += 1
    print(" " * (size-1) + char[size-1]) 
    

if __name__ == "__main__":
    spruce(5)