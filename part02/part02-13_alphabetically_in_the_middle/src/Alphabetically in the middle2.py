first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if second < first < third:
    print(f"The letter in the middle is {first}")

elif third < first < second:
    print(f"The letter in the middle is {first}")
    
elif first < second < third:
    print(f"The letter in the middle is {second}")

elif third < second < first:
    print(f"The letter in the middle is {second}")
    
elif first < third < second:
    print(f"The letter in the middle is {third}")

elif second < third < first:
    print(f"The letter in the middle is {third}")