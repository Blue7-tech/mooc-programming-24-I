characters = input("Write text: ")
char_list = characters.split(" ")
with open("wordlist.txt") as file:
    word_list = []
    for line in file:
        line = line.strip()
        word_list.append(line)
    
result = []
for word in char_list:
    for word2 in word_list:
        if word.lower() == word2:
            print(f"{word} ", end = "")
            a = False
            break    
    if a:
        print(f"*{word}* ", end = "")
    a = True

print()
