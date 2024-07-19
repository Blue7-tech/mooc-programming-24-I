password = input("Password:")

while True:
    repeat_password = input("Repeat Password:")

    if repeat_password != password:
        print("They do not match!")

    elif repeat_password == password:
        print("User account created!")
        break
