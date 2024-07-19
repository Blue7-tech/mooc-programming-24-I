# write your solution here
def wordlist():

    words = []

 

    with open("wordlist.txt") as file:

        for row in file:

            words.append(row.strip())

 

    return words

 

words = wordlist()

sentence = input("Write text: ")

 

for word in sentence.split(' '):

    if word.lower() in words:

        print(word + " ", end="")

    else:

        print("*" + word + "* ", end="")

print()

"""string_element = input("Write text:")

words = []

with open("wordlist.txt") as file:
    for line in file:
        words.append(line.strip())


temp2 = string_element.split()        
written = []

for word in temp2:
    written.append(word.lower())

b = 0
for i in range(0,len(string_element)):
    if string_element[i] == " ":
        b = i
        break     

temp = ""
i = 1
for word in written:
    if i == 1 and word == string_element[:b] and word in words:
        temp += word + " "
    elif i == 1 and word != string_element[:b] and word in words:
        temp += word[0].upper() + word[1:] + " "
    elif i > 1 and word in words:
        temp += word + " " 
    elif word not in words:
        temp += "*" + word + "*" + " "
    i += 1    

print(temp)"""






sentence = input("Write text: ")
sentence = sentence.strip(".")
sentence = sentence.strip("?")
sentence = sentence.strip(",")
sentence = sentence.strip(" ")
sentence_list = sentence.split(" ")

word_list = []

with open("wordlist.txt") as file:
    for word in file:
        word = word.replace("\n", "")
        word_list.append(word)

for word in sentence_list:
    if word.lower() in word_list:
        print(word, end = " ")
    else:
        print(f"*{word}*", end = " ")   