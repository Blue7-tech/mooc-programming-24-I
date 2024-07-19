name_1 = input("Name:")
age_1 = int(input("Age:"))
name_2 = input("Name:")
age_2 = int(input("Age:"))

if age_1 > age_2:
    print(f"The elder is {name_1}")

if age_2 > age_1:
    print(f"The elder is {name_2}")

if age_2 == age_1:
    print(f"{name_1} and {name_2} are the same age")