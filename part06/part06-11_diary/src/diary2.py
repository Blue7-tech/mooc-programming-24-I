while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    command = int(input("Function: "))
    
    if command == 1:
        entry = input("Diary entry: ")
        print("Diary saved")
        with open("diary.txt", "a") as file:
            file.write(entry+"\n")
    elif command == 2:
        print("Entries:")
        with open("diary.txt") as file:
            contents = file.read()
            print(contents)
    elif command == 0:
        print("Bye now!")
        break
        
            