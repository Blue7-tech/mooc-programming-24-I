# Write your solution here

def times_ten(start_index: int, end_index: int):
    times_ten = {}
    for i in range(start_index, end_index+1):
        times_ten[i] = i*10
    
    return times_ten

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)       