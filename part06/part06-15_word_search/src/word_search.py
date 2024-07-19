# Write your solution here
def get_words():
    words = []
    with open("words.txt") as file:
        for word in file:
            words.append(word.strip())
    
    return words
    
def find_words(search_term: str):
    words = get_words()
    found = []
    if "." in search_term:                           
        for word in words:
            if len(word) == len(search_term):
                for i in range(len(word)):
                    if word[i] != search_term[i] and search_term[i] == ".":
                        a = True
                        continue
                    elif word[i] == search_term[i]:
                        a = True
                        continue
                    else:
                        a = False
                        break
                if a:
                    found.append(word)

        return found      
        
    elif search_term.startswith("*"):
        search_term = search_term[1:]
        for word in words:
            if word.endswith(search_term):
                found.append(word)

        return found
        
    elif search_term.endswith("*"):
        search_term = search_term[:-1]  
        for word in words:
            if word.startswith(search_term):
                found.append(word)

        return found
    
    else:
        for word in words:
            if word == search_term:
                found.append(word)

        return found
             
if __name__ == "__main__":
    print(find_words("ca.b."))