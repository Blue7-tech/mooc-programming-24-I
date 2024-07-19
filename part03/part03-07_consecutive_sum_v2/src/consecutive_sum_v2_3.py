limit = int(input("Upper limit: "))

string = ""
sum1 = 1
number = 2
i = 0       
while sum1 < limit:
    if sum1 == 1:
        string += f"{sum1} + {number}" 
    elif sum1 > 1:
        string += f" + {number}"    
    sum1 += number
    number += 1
    
    
print(sum1)
print(string + " = " + str(sum1))