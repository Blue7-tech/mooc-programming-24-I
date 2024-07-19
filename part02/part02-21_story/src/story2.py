temp = ""
sum = ""
while True:
    word = input("Please type in a word: ")
    if word == "end":
        sum = sum.strip()
        break
    elif word == temp:
        break
    sum += word + " "
    temp = word
    
print(sum)