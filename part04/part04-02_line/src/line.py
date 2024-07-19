# Write your solution here
# You can test your function by calling it within the following block

def line(a, b):
    if b == "":
        print(f"{a * "*"}")
        
    else:
        print(f"{a * b[0]}")
    
if __name__ == "__main__":
    line(5, "")