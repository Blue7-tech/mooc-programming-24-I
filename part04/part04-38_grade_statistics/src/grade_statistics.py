def input_from_user():
    points_exercises = ""
    
    while True:
        user_input = input("Exam points and completed exercises completed:")
        points_exercises += user_input + " "
        if user_input == "":
            break

    return points_exercises.split()

def exam_points(list: list):
    exam_points = []
    index = (len(list)//2)
    
    for i in list:
        exam_points.append(int(i))
    for i in range(1, index+1, 1):
        exam_points.pop(i)
        
    return exam_points

def exercise_points(list: list):
    exercise_points = []
    int_list = []
    index = (len(list)//2)
    
    for i in list:
        int_list.append(int(i))
    for i in range(0, index, 1):
        int_list.pop(i) 
    for i in int_list:
        exercise_points.append(i // 10)    
         
    return exercise_points   

def total_points(exam_points, exercise_points: list):   
    total_points = []
    index = (len(list)//2)
    i = 1
    a = 0
    while i <= index:    
        total_points.append(exam_points[a] + exercise_points[a])
        i += 1
        a += 1
    return total_points
        
def total_points2(exam_points, exercise_points: list):   
    total_points2 = []
    index = (len(list)//2)
    i = 1
    a = 0
    while i <= index:
        if exam_points[a] < 10:
            exam_points[a] = 0     
        total_points2.append(exam_points[a] + exercise_points[a])
        i += 1
        a += 1
    return total_points2

def grade(total_points2: list):
    grade = [] 
    for i in total_points2:
        if 0 <= i <= 14:
            grade.append(0)        
        if 15 <= i <= 17:
            grade.append(1)
        if 18 <= i <= 20:
            grade.append(2)
        if 21 <= i <= 23:
            grade.append(3)
        if 24 <= i <= 27:
            grade.append(4)
        if 28 <= i <= 30:
            grade.append(5)
    return grade           

def pass_percentage(grade: list):
    grade_above_0 = []    
    for i in grade:
        if i == 0:
            continue
        grade_above_0.append(i)     
    pass_percentage = len(grade_above_0)/len(grade) * 100
    return pass_percentage

def points_average(total_points: list):
    points_average = sum(total_points)/len(total_points) 
    return points_average

def main(points_average, pass_percentage, grade: list):
    grade5 = ['  5: ']
    grade4 = ['  4: ']
    grade3 = ['  3: ']
    grade2 = ['  2: ']
    grade1 = ['  1: ']
    grade0 = ['  0: ']
    
    for i in grade:
        if i == 5:
            grade5.append('*')
        if i == 4:
            grade4.append('*')
        if i == 3:
            grade3.append('*')
        if i == 2:
            grade2.append('*')
        if i == 1:
            grade1.append('*')
        if i == 0:
            grade0.append('*')
    
    grade_5 = "".join(grade5)
    grade_4 = "".join(grade4)
    grade_3 = "".join(grade3)
    grade_2 = "".join(grade2)
    grade_1 = "".join(grade1)
    grade_0 = "".join(grade0) 
    
    print(f"""Statistics:
Points average: {points_average:.1f} 
Pass percentage: {pass_percentage:.1f}
Grade distribution:
{grade_5}
{grade_4}
{grade_3}
{grade_2}
{grade_1}
{grade_0}
""")                    

list = input_from_user()
exam_point = exam_points(list)
exercise_point = exercise_points(list)
total_point = total_points(exam_point, exercise_point)
total_point2 = total_points2(exam_point, exercise_point)
grades = grade(total_point2)
passed = pass_percentage(grades)
average = points_average(total_point)

main(average, passed, grades)




   






   