
        

# Write your solution here
import random

def generate_password(number: int):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    password = ""
    for i in range(number):
        password += alphabet[random.randint(0,25)]
    return password
    
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))