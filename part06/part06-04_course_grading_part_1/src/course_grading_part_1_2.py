if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students4.csv"
    exercise_data = "exercises4.csv"

with open(student_info) as file1, open(exercise_data) as file2:
    
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
    
    for identifier in id_name:
        print(f"{id_name[identifier]} {id_exercises[identifier]}") 
    
  
    
