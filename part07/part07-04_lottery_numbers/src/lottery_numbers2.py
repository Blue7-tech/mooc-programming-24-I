
        
# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    weekly_draw = random.sample(number_pool, amount)
  
    
    return sorted(weekly_draw)
    
if __name__ == "__main__":
    
    for number in lottery_numbers(3, 2, 22):
        print(number)