# Write your solution here
import fractions

def fractionate(amount: int):
    fractionate = []
    for i in range(amount):
        fractionate.append(fractions.Fraction(numerator=1, denominator=amount))
   
    return fractionate
if __name__ == "__main__":    
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))
       