def input_from_user():
    students_results = []
    while True:
        results = input("Exam points and exercises completed: ")
        if results == "":
            break
        student = results.split(" ")      
        student[0] = int(student[0])
        student[1] = int(student[1])
        students_results.append(student)
    return students_results
        
def exercise_points(students_results: list):
    exercise_points = []
    for student in students_results:
        points = student[1] // 10
        exercise_points.append(points)
    return exercise_points

def points_average(students_results, exercise_points):
    total_points = []
    for i in range(len(students_results)):
        points = students_results[i][0] + exercise_points[i]
        total_points.append(points)
    return sum(total_points)/len(total_points)

def grading(students_results, exercise_points):
    total_points = []
    for i in range(len(students_results)):
        if students_results[i][0] < 10:
            total_points.append(0)
            continue
        points = students_results[i][0] + exercise_points[i]
        total_points.append(points)
    
    grades = []
    for points in total_points:
        if points <= 14:
            grades.append(0)
        elif points <= 17:
            grades.append(1)
        elif points <= 20:
            grades.append(2)
        elif points <= 23:
            grades.append(3)
        elif points <= 27:
            grades.append(4)
        elif points <= 30:
            grades.append(5)
    return grades

def pass_percentage(grades):
    not_passed = grades.count(0)
    return (len(grades)-not_passed)/len(grades)*100


exam_exercise_points = input_from_user()
points = exercise_points(exam_exercise_points)
final_results = grading(exam_exercise_points, points)

points_average = points_average(exam_exercise_points, points)

passed_percentage = pass_percentage(final_results)
print()
print("Statistics:")
print(f"Points average: {points_average:.1f}")
print(f"Pass percentage: {passed_percentage:.1f}")
print(f"""Grade distribution:
  5: {final_results.count(5)*"*"}
  4: {final_results.count(4)*"*"}   
  3: {final_results.count(3)*"*"}  
  2: {final_results.count(2)*"*"}  
  1: {final_results.count(1)*"*"}  
  0: {final_results.count(0)*"*"}         
""")

    