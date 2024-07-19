string = input("Word:")

if len(string) % 2 == 0:
    print("*"*30)
    print("*" + " " * (14-(len(string)//2)) + string + " " * (14-(len(string)//2)) + "*")
    print("*"*30)

else:
    print("*"*30)
    print("*" + " " * (14-(len(string)//2)-1) + string + " " * (14-(len(string)//2)) + "*")
    print("*"*30)