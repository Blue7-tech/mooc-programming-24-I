points = int(input("How many points [0-100]:"))

if points < 0:
    print("impossible")

if 0 <= points <= 49:
    print("fail")