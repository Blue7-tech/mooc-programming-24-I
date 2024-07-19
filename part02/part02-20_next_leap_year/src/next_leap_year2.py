year = int(input("Please type in a year: "))

if year % 4 == 0 and year % 100 != 0:
    if (year+4) % 4 == 0 and (year+4) % 100 != 0:
        print(f"The next leap year after {year} is {year+4}")
    elif (year+4) % 4 == 0 and (year+4) % 100 == 0 and (year+4) % 400 == 0:
        print(f"The next leap year after {year} is {year+4}")
    else:
        print(f"The next leap year after {year} is {year+8}")
        
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"The next leap year after {year} is {year+4}")

else:        
    no_leap_year = year
    while True:
        if no_leap_year % 4 == 0 and no_leap_year % 100 != 0:
            print(f"The next leap year after {year} is {no_leap_year}")
            break
        elif no_leap_year % 4 == 0 and no_leap_year % 100 == 0 and no_leap_year % 400 == 0:
            print(f"The next leap year after {year} is {no_leap_year}")
            break
        else:
            no_leap_year += 1