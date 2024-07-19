# Write your solution here
def factorials(n: int):
    
    factorials = {}
    
    for i in range(1,n+1):
        factorials[i] = 1
        if i > 1:
            temp = 1
            for j in range(1,i+1):
                temp *= j
            factorials[i] = temp
             
    return factorials        


if __name__ == "__main__":
    k = factorials(5)  
    print(k[1])
    print(k[2])
    print(k[3])
    print(k[4])
    print(k[5])   