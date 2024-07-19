import string
import random

def generate_password(number: int):
    letters = string.ascii_lowercase
    password = ""
    for i in range(number):
        password += random.choice(letters)
    
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))