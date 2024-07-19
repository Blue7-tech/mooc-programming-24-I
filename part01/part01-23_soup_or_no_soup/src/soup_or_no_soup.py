name = input("Please tell me your name:")

if name != "Jerry":
    portions = int(input("How many portions of soup?"))
    price_portion = 5.90
    price = price_portion * portions
    print(f"""The total cost is {price}
Next please! """)

else:
    print("Next please!")
