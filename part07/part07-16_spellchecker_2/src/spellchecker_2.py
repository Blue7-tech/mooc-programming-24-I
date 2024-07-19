# Write your solution here
from difflib import get_close_matches

sentence = input("Write text: ")
sentence_list = sentence.split(" ")

word_list = []

with open("wordlist.txt") as file:
    for word in file:
        word = word.replace("\n", "")
        word_list.append(word)


wrong_words = {}
for word in sentence_list:
    if word.lower() in word_list:
        print(word, end = " ")
    else:
        wrong_words[word] = get_close_matches(word, word_list, n=3, cutoff = 0.6)
        print(f"*{word}*", end = " ")

print()
print("suggestions:")
for word in wrong_words:
    temp = ", ".join(wrong_words[word])
    print(f"{word}: {temp}")

        

     