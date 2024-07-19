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
    file = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_name = "course1.txt"   

with open(student_info) as file1, open(exercise_data) as file2, open(exam_data) as file3, open(course_name) as file4, open("results.txt", "w") as file5, open("results.csv", "w") as file6:
    
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
    
    header = ""
    for line in file4:
        line = line.strip()
        if line[0] == "n":
            line = line[6:] + ", "
            header += line
        else:
            line = line[-1]
            header += line + " credits"
    
    file5.write(header+"\n")
    file5.write(len(header)*"="+"\n")
    word = "name"
    word1 = "exec_nbr"
    word2 = "exec_pts."
    word3 = "exm_pts."
    word4 = "tot_pts."
    word5 = "grade"
    file5.write(f"{word:30}{word1:10}{word2:10}{word3:10}{word4:10}{word5:10}\n")
    for identifier in id_name:
        file5.write(f"{id_name[identifier]:30}{id_exercises[identifier]:<10}{id_exercises[identifier]//4:<10}{id_exams[identifier]:<10}{id_exercises[identifier]//4 + id_exams[identifier]:<10}{grading((id_exercises[identifier]//4) + id_exams[identifier]):<10}\n") 
        file6.write(f"{identifier};{id_name[identifier]};{grading((id_exercises[identifier]//4) + id_exams[identifier]):<10}\n")
    
