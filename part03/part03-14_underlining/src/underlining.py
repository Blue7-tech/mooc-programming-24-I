string = ""

while string != " ":
    string = input("Please type a string:")
    print(string)
    under_score = len(string) * "-"
    print(under_score)
    if string == "":
        break


