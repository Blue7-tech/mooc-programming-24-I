# Write your solution here

def new_person(name: str, age: int):
    
    new_person = (name, age)
    if " " not in name or name == "" or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("name is an empty string or name contains less than two words or name is longer than 40 characters or age is a negative number or age is greater than 150")  
    return new_person
    
if __name__ == "__main__":
    print(new_person("Andrew", 161))
    
