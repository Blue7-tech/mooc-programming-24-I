def find_words(search_term: str):
    result = []
    with open("words.txt") as file:        
        if "." in search_term:
            for word in file:
                word_modified = word.replace("\n", "")
                if len(word_modified) == len(search_term):
                    temp = ""
                    a= 0
                    b = 0
                    while a < len(word_modified):
                        if word_modified[a] == search_term[b]:
                            temp += word_modified[a]
                            a += 1
                            b += 1    
                        elif search_term[b] == ".":
                            temp += word_modified[a]
                            a += 1
                            b += 1 
                        else:
                            break
                    if len(temp) == len(search_term):
                        result.append(temp)
                        
        elif "." and "*" not in search_term:
            for word in file:
                word_modified = word.replace("\n", "")
                if word_modified == search_term:
                    result.append(word_modified)
        
        elif search_term.startswith("*"):
            for word in file:
                word_modified = word.replace("\n", "")
                word_reversed = word_modified[::-1]
                search_term_reversed = search_term[::-1]
                a = 0
                b = 0
                temp_reversed = ""
                while a < len(word_reversed):
                    if word_reversed[a] == search_term_reversed[b]:
                        temp_reversed += word_reversed[a]
                        a += 1
                        b += 1
                    elif search_term_reversed[b] == "*":
                        temp_reversed += word_reversed[a]
                        a += 1
                    else:
                        break
                if len(temp_reversed) >= len(search_term_reversed):
                    temp = temp_reversed[::-1]
                    result.append(temp)        
        
        elif search_term.endswith("*"):
            for word in file:
                word_modified = word.replace("\n", "")
                a = 0
                b = 0
                temp = ""
                while a < len(word_modified):
                    if word_modified[a] == search_term[b]:
                        temp += word_modified[a]
                        a += 1
                        b += 1
                    elif search_term[b] == "*":
                        temp += word_modified[a]
                        a += 1
                    else:
                        break
                if len(temp) >= len(search_term):
                    result.append(temp)
                
    return result
 
if __name__ == "__main__":
    print(find_words("ca.b."))