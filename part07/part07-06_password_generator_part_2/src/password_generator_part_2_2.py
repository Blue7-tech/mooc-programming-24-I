
        

import random

def generate_strong_password(length: int, number: bool, spec_char: bool):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    punctuation = ["!", "?", "=", "+", "-", "(", ")", "#"]     
    password = ""

    index = 0
    for i in range(length):
        if number and spec_char:
            if length == 3:
                rndm_pw_character = [alphabet[random.randint(0,25)], str(random.randint(0,9)), punctuation[random.randint(0,7)]]
                password += rndm_pw_character[index]
                index += 1
            elif length > 3: 
                if index > 2:
                    rndm_pw_character = [alphabet[random.randint(0,25)], str(random.randint(0,9)), punctuation[random.randint(0,7)]]
                    password += random.choice(rndm_pw_character)
                    continue 
                rndm_pw_character = [alphabet[random.randint(0,25)], str(random.randint(0,9)), punctuation[random.randint(0,7)]]
                password += rndm_pw_character[index]
                index += 1
                       
        
        elif not number and spec_char:
            if length == 3:
                if index > 1:
                    password += random.choice(rndm_pw_character)
                    continue
                rndm_pw_character = [alphabet[random.randint(0,25)], punctuation[random.randint(0,7)]]
                password += rndm_pw_character[index]
                index += 1
                
            elif length > 3: 
                if index > 1:
                    rndm_pw_character = [alphabet[random.randint(0,25)], punctuation[random.randint(0,7)]]
                    password += random.choice(rndm_pw_character)
                    continue 
                rndm_pw_character = [alphabet[random.randint(0,25)], punctuation[random.randint(0,7)]]
                password += rndm_pw_character[index]
                index += 1
    
        elif number and not spec_char:
            if length == 3:
                if index > 1:
                    password += random.choice(rndm_pw_character)
                    continue
                rndm_pw_character = [alphabet[random.randint(0,25)], str(random.randint(0,9))]
                password += rndm_pw_character[index]
                index += 1
            elif length > 3: 
                if index > 1:
                    rndm_pw_character = [alphabet[random.randint(0,25)], str(random.randint(0,9))]
                    password += random.choice(rndm_pw_character)
                    continue 
                rndm_pw_character = [alphabet[random.randint(0,25)], str(random.randint(0,9))]
                password += rndm_pw_character[index]
                index += 1
        
        else:
            password += alphabet[random.randint(0,25)]
    
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, False, True))