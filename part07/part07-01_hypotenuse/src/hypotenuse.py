# Write your solution here


def hypotenuse(leg1: float, leg2: float):
    from math import sqrt
    
    hypotenuse = sqrt(leg1**2+leg2**2)
    
    return hypotenuse
    
    
if __name__ == "__main__":
    print(hypotenuse(5.6, 9.2))