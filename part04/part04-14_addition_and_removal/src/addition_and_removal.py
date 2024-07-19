# Write your solution here

list = []

print(f"The list is now {list}")

command = ""
i = 1


while command != "x":
    command = input("a(d)d, (r)emove or e(x)it:")
    
    if command == "d":
        list.append(i)
        print(f"The list is now {list}")
        i += 1
    elif command == "r":
        i -= 1
        list.pop(i-1)
        print(f"The list is now {list}")
    elif command == "x":
        print("Bye!")
    