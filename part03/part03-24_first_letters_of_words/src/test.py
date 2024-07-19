sent = input("Please type in a sentence:")
iteration = sent.count(" ")
i = 0
k = 0

while i <= iteration:
    print(sent[k])
    k = sent.find(" ", k) + 1
    i += 1