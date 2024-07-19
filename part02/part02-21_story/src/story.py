words = ''
second_word = ""

while True:
    word = input('Please typ a word: ')
    if word == "end":
        break
    elif second_word == word:
        break
    else:
        words += word + " "
        second_word = word


print(words)
