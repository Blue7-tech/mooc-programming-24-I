def squared(char: str, number:int):
    
    i=0
    while i < number*number:
        if i % number == 0:
            print()
        print(char[i%len(char)], end = "")
        i += 1
        
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)