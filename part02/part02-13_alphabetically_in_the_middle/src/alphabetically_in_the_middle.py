first_letter = input("1st letter:")
second_letter = input("2nd letter:")
third_letter = input("3rd letter:")

if second_letter <= first_letter <= third_letter:
    print(f"The letter in the middle is {first_letter}")

if third_letter <= first_letter <= second_letter:
    print(f"The letter in the middle is {first_letter}")

elif first_letter <= second_letter <= third_letter:
    print(f"The letter in the middle is {second_letter}")

if third_letter <= second_letter <= first_letter:
    print(f"The letter in the middle is {second_letter}")

elif first_letter <= third_letter <= second_letter:
    print(f"The letter in the middle is {third_letter}")
if second_letter <= third_letter <= first_letter:
    print(f"The letter in the middle is {third_letter}")

