# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print(f"""Your bonus is 10 %
You now have {points}""")

else:
    points *= 1.15
    print(f"""Your bonus is 15 %
You now have {points}""")