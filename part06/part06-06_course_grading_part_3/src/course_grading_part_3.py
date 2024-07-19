# tee ratkaisu tänne

student_data = input("Student information: ")

exercise_data = input("Exercises completed: ")

exam_data = input("Exam points: ")

 

def grade(points:int):

    a = 0

    limits = [15, 18, 21, 24, 28]

    while a < 5 and points >= limits[a]:

        a += 1

 

    return a

 

def to_points(number:int):

    return number // 4

 

students = {}

with open(student_data) as file:

    for row in file:

        parts = row.split(";")

        if parts[0] == "id":

            continue

        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

 

exercises = {}

with open(exercise_data) as file:

    for row in file:

        parts = row.split(";")

        if parts[0] == "id":

            continue

        esum = 0

        for i in range(1, 8):

            esum += int(parts[i])

        exercises[parts[0]] = esum

 

exams = {}

with open(exam_data) as file:

    for row in file:

        parts = row.split(";")

        if parts[0] == "id":

            continue 

        esum = 0

        for i in range(1, 4):

            esum += int(parts[i])

        exams[parts[0]] = esum

name = "name"
exec_nbr = "exec_nbr"
exec_pts = "exec_pts."
exm_pts = "exm_pts."
tot_pts = "tot_pts."
test = "grade"

print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{test:10}")

for student_id, name in students.items():
    total_points = to_points(exercises[student_id]) + exams[student_id]
    print(f"{name:30}{exercises[student_id]:<10}{to_points(exercises[student_id]):<10}{exams[student_id]:<10}{total_points:<10}{grade(total_points):<10}")
    
    
    


