# Write your solution here
import string
import random

def generate_strong_password(number: int, bool1, bool2):
    letters = string.ascii_lowercase
    digits = string.digits
    special_char = "!?=+-()#"
    password = ""
    
    for i in range(number):
        if not bool1 and not bool2:
            password += random.choice(letters)
        elif bool1 and not bool2:
            mod = letters + digits
            password += random.choice(mod)
        elif not bool1 and bool2:
            mod = letters + special_char
            password += random.choice(mod)
        elif bool1 and bool2:
            mod = letters + digits + special_char
            password += random.choice(mod)
    
    """if bool1 and not bool2:
        for digit in digits:
            if digit in password:
                return password 
    
        password = password[:-1]
        password += random.choice(digits)
        return password
    
    elif not bool1 and bool2:
        for special in special_char:
            if special in password:
                return password 
        password = password[:-1]
        password += random.choice(special_char)
        return password
    
    elif bool1 and bool2:
        for special in special_char:
            for digit in digits:
                if special and digit in password:
                    return password 

        for letter in letters:
            if letter in password:
                return password
        password = password[:-1]
        password += random.choice(special_char)
        return password

        for digit in digits:
            if digit in password:
                return password 
    
        password = password[:-1]
        password += random.choice(digits)
        return password
        
    for letter in letters:
        if letter in password:
            return password 
    
    password = password[:-1]
    password += random.choice(letters)"""
    return password        

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(3, True, True))