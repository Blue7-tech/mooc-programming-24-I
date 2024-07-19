from difflib import get_close_matches

characters = input("Write text: ")
char_list = characters.split(" ")
with open("wordlist.txt") as file:
    word_list = []
    for line in file:
        line = line.strip()
        word_list.append(line)
    
fails = []
for word in char_list:
    for word2 in word_list:
        if word.lower() == word2:
            print(f"{word} ", end = "")
            a = False
            break    
        a = True
    if a:
        fails.append(word)
        print(f"*{word}* ", end = "")
    
print("sugesstions:")
suggestions = []
for fail in fails:
    temp = get_close_matches(fail, word_list)
    suggestions.append(temp)

i = 0
for fail in fails:
    print(f"{fail}: {", ".join(suggestions[i])}")
    i += 1