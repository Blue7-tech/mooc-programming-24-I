def hash_square(length:int):
    hasq_element = "#"
    hasq_element_mod = hasq_element * length
    for i in range(length):
        print(hasq_element_mod)
        
if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)