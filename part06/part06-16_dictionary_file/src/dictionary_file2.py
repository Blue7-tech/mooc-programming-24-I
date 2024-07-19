
    
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    command = int(input("Function: "))
    
    if command == 1:
        word_fin = input("The word in Finnish:")
        word_eng = input("The word in English:")
        print("Dictionary entry added")
        with open("dictionary.txt", "a") as file:
            file.write(f"{word_fin} - {word_eng}\n")
    
    elif command == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt", "r") as file:
            for line in file:
                line = line.strip()
                if search_term in line:
                    print(line)
    
    elif command == 3:
        print("Bye!")