number = int(input("Please type in a number:"))
fac1 = 1
fac2 = 1
i = 0
while i < number*number:
    print(f"{fac1} x {fac2} = {fac1*fac2}")
    fac2 += 1
    if fac2 == number+1:
        fac2 = 1
        fac1 += 1
    i += 1