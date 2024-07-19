# write your solution here
names = {}
courses_completed = {}

file1 = input("Student infromation:")
file2 = input("Exercises completed:")

with open(file1) as file1:
    for line in file1:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        temp = ""
        for name in range(1,3):
            temp += parts[name] + " "    
        names[int(parts[0])] = temp.strip()

with open(file2) as file2:
    for line in file2:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        temp = 0
        for exercises in range(1,8):
            temp += int(parts[exercises]) 
        courses_completed[int(parts[0])] = temp
    
for pic, name in names.items():
    if pic in courses_completed:
        compl = courses_completed[pic]
    print(f"{name} {compl}")           

 