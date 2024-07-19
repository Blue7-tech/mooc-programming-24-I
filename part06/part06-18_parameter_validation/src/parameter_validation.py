# Write your solution here

def new_person(name: str, age: int):
    
    if " " in name and name != "" and len(name) < 40 and age > 0 and age < 150:
        return name, age
    else:
        raise ValueError
        
if __name__ == "__main__":
    print(new_person("Andrew", 32))
