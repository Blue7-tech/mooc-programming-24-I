def squared(letter: str, count: int):
    
    iteration_print = count
    
    i = 0
    k = 0
    l = ""
    while i < count:
        while k < count*count:
            if k == iteration_print+1:
                iteration_print += count+1
                break
            l += letter[k%len(letter)]
            k += 1
        print(l)
        l = ""
        i += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)