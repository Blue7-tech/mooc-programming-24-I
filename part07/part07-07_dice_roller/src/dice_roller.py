import random
# Write your solution here
def roll(die: str):
    dieA = [3,3,3,3,3,6]
    dieB = [2,2,2,5,5,5]
    dieC = [1,4,4,4,4,4]
    
    if die == "A":
        return random.choice(dieA)
    elif die == "B":
        return random.choice(dieB)
    elif die == "C":
        return random.choice(dieC)
    
def play(die1: str, die2: str, times: int):
    
    results = [0,0,0]
    for i in range(times):
        number1 = roll(die1)
        number2 = roll(die2)
        if number1 > number2:
            results[0] += 1
        elif number2 > number1:
            results[1] += 1
        else:
            results[2] += 1
            
    return results[0],results[1],results[2]
    
if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)