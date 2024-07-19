# write your solution here

names = {}
courses_completed = {}
exam_points = {}

file1 = input("Student infromation:")
file2 = input("Exercises completed:")
file3 = input("Exam points:")
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
        
with open(file3) as file3:
    for line in file3:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        temp = 0
        for exam in range(1,4):
            temp += int(parts[exam]) 
        exam_points[int(parts[0])] = temp

name = "name"
exec_nbr = "exec_nbr"
exec_pts = "exec_pts."
exm_pts = "exm_pts."
tot_pts = "tot_pts."
test = "grade"
print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{test:10}")    
for pic, name in names.items():
    if pic in courses_completed:
        exercise_nmbr = courses_completed[pic]
        exercise_points = exercise_nmbr // 4
    if pic in exam_points:
        exam_point = exam_points[pic]
    total_points = exercise_points + exam_point
    if 0 <= total_points <= 14:
         grade = 0 
    if 15 <= total_points <= 17:
         grade = 1 
    if 18 <= total_points <= 20:
         grade = 2 
    if 21 <= total_points <= 23:
         grade = 3 
    if 24 <= total_points <= 27:
         grade = 4 
    if 28 <= total_points :
         grade = 5    
    print(f"{name:30}{exercise_nmbr:<10}{exercise_points:<10}{exam_point:<10}{total_points:<10}{grade:<10}")  


"""names = {}
courses_completed = {}
exam_points = {}

file1 = input("Student infromation:")
file2 = input("Exercises completed:")
file3 = input("Exam points:")
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
        exercise_points = temp // 4 
        courses_completed[int(parts[0])] = exercise_points
        
with open(file3) as file3:
    for line in file3:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        temp = 0
        for exam in range(1,4):
            temp += int(parts[exam]) 
        exam_points[int(parts[0])] = temp

    
for pic, name in names.items():
    if pic in courses_completed:
        exercise_points = courses_completed[pic]
    if pic in exam_points:
        exam_point = exam_points[pic]
    total_points = exercise_points + exam_point
    if 0 <= total_points <= 14:
         print(f"{name} 0") 
    if 15 <= total_points <= 17:
         print(f"{name} 1")
    if 18 <= total_points <= 20:
         print(f"{name} 2")
    if 21 <= total_points <= 23:
         print(f"{name} 3")
    if 24 <= total_points <= 27:
         print(f"{name} 4")
    if 28 <= total_points :
         print(f"{name} 5")"""                
