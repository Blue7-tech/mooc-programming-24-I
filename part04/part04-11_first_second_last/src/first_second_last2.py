def first_word(sentence: str):
    index1 = sentence.find(" ")
    return sentence[:index1]

def second_word(sentence: str):
    index1 = sentence.find(" ")
    index1 += 1
    index2 = sentence.find(" ", index1)
    if index2 == -1:
        return sentence[index1:]
    else:
        return sentence[index1:index2]

def last_word(sentence: str):
    count = sentence.count(" ")
    index = 0
    i = 1
    while i <= count:
        index_last = sentence.find(" ", index)
        index = index_last
        index += 1
        i += 1
    return sentence[index:]

if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence)) # it
    print(second_word(sentence)) # was
    print(last_word(sentence)) # python