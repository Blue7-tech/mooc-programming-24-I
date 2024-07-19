
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function:"))

    if function == 1:
        diary_entry = input("Diary entry: ")
        print("Diary saved" "\n")
        
        with open("diary.txt", "a") as my_file:
            my_file.write(diary_entry + "\n")
            
    elif function == 2:
        with open("diary.txt") as my_file:
            print("Entries:")
            for line in my_file:
                print(line.replace("\n", ""))
            
    elif function == 0:
        print("Bye now!")
        break

    
        
        
    