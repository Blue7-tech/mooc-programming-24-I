def factorials(n: int):
    dict_fac = {}
    
    i = 1
    k = 1
    l = 1
    while l <= n:
        dict_fac[l] = 0
        i *= k
        dict_fac[l] = i
        k += 1 
        l += 1
        
    return dict_fac
        
if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])