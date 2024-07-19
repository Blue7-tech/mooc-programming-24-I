import random 

def lottery_numbers(amount: int, lower: int, upper: int):
    pool = []
    for i in range(lower, upper+1):
        pool.append(i)
        
    result = []
    for i in range(amount):
        result.append(random.choice(pool))
        pool.remove(result[-1])
        
    result.sort()
    return result

if __name__ == "__main__":
    for number in lottery_numbers(3, 2, 22):
        print(number)