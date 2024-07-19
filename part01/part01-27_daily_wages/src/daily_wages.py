wage = float(input("Hourly wage:"))
hours = float(input("Hours worked:"))
day = input("Day of the week:")

if day.lower() != "sunday":
    print(f"Daily wages: {wage * hours} euros") 

else:
    wage *= 2
    daily_wage = wage * hours
    print(f"Daily wages: {wage * hours} euros") 