# Write your solution here
def first_word(sentence):
    i = 0
    while sentence[i] != " ":
        i += 1
    return sentence[:i]
    
    
def second_word(sentence):
    x = len(sentence)-1
    i = 0
    while sentence[i] != " ":
        i += 1
    
    k = i + 1 
    while sentence[k] != " ":
        k += 1
        if k == x:
            return sentence[i+1:]
    return sentence[i+1:k]
    
def last_word(sentence):
    x = len(sentence)-1
    
    while sentence[x] != " ":
        x -= 1
    return sentence[x+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))