number = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
week = float(input("How much money do you spend on groceries in a week?"))

weekly = number * price + week
daily = weekly / 7

print(f"""Daily: {daily} euros
Weekly: {weekly} euros""")