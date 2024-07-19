numbers = []
add = 1

while True:
    print(f"The list is now {numbers}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "d":
        numbers.append(add)
        add += 1
    elif command == "r":
        numbers.pop()
        add -= 1
    elif command == "x":
        print("Bye!")
        break