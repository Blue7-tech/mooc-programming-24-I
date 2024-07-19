attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1

    if code == "4321":
        success = True
        break

    print("Wrong")

if success and attempts == 1:
    print(f"Correct! It only took you one single attempt!")

else:
    print(f"Correct! It took you {attempts} attempts")