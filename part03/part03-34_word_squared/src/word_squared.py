# Write your solution here
def squared(x: str, y: int):
    i=0
    k=0
    index = 0
    while  i < y:
        temp = ""
        while  k < y:
            if index == len(x):
                index = 0
            temp += x[index]
            index += 1
            k += 1
        k = 0
        print(temp)
        i += 1 

if __name__  == "__main__":
    squared("aybabtu", 5)

