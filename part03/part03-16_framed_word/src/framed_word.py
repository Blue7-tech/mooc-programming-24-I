string = input("Word:")
x = len(string)
c = x // 2
b = 14 - c
y = 30

if x <= 30 and x % 2 == 0:
    print("*" * 30)
    result = "*" + b * " " + string + b * " " + "*"
    print(result)
    print("*" * 30)

elif x <= 30 and x % 2 != 0:
    f = b - 1
    print("*" * 30)
    result = "*" + f * " " + string + b * " " + "*"
    print(result)
    print("*" * 30)