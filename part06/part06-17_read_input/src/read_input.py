# Write your solution here

def read_input(string: str, integer1: int, integer2: int):
    while True:
        argument1 = integer1
        argument2 = integer2
        
        try:
            number = int(input(string))
        
        except ValueError:
            number = -1    
            
        if argument1 <= number <= argument2:
            return number
            break
        else:
            print(f"You must type in an integer between {integer1} and {integer2}")
       
    
if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)