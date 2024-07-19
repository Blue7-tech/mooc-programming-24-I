number = int(input("input(Please type in a number: "))

k = 1   
while k < number:
    print(k+1)
    print(k)    
    k+=2
    if number % 2 != 0 and k >= number:
        print(k)
        