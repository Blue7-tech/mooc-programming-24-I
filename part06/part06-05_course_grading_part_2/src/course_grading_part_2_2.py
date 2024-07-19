def grading(points: int):
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students4.csv"
    exercise_data = "exercises4.csv"
    exam_data = "exam_points4.csv"   

with open(student_info) as file1, open(exercise_data) as file2, open(exam_data) as file3:
    
    id_name = {}
    for line in file1:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id_int = int(parts[0])
        full_name = parts[1:]
        full_name_joined = " ".join(full_name)
        id_name[id_int] = full_name_joined.strip()
    
    id_exercises = {}
    for line in file2:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id_int = int(parts[0])
        temp2 = []
        temp = parts[1:]
        for part in temp:
            temp2.append(int(part))
        id_exercises[id_int] = sum(temp2)
        
    id_exams = {}
    for line in file3:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id_int = int(parts[0])
        temp2 = []
        temp = parts[1:]
        for part in temp:
            temp2.append(int(part))
        id_exams[id_int] = sum(temp2)
    
    for identifier in id_name:
        print(f"{id_name[identifier]} {grading((id_exercises[identifier]//4) + id_exams[identifier])}") 