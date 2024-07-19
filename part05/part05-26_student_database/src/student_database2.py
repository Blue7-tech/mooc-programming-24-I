def add_student(students, name):
    students[name] = []

def calculate_grade(students, name):
    sum_courses = 0
    for course in students[name]:
        sum_courses += course[1]
        
    return sum_courses/len(students[name])

def print_student(students, name):      
    if students[name] == []:
        print(f"""{name}:
no completed courses""")
    elif students[name] != []:
        grade = calculate_grade(students, name)
        print(f"""{name}:
 {len(students[name])} completed courses:""")
        for course in students[name]:
            print(f"  {course[0]} {course[1]}")
        print(f" average grade {grade:.1f}")           
    else:
        print(f"""{name}: no such person in the database""")

def add_course(students: dict, name: str, course: tuple):
    to_del = 0
    
    if course[1] != 0:
        students[name].append(course)
    
    if len(students[name]) > 1:
        to_check = course
        for comp_course in students[name]:
            if comp_course[0] == to_check[0] and comp_course[1] != to_check[1]:
                if comp_course[1] > to_check[1]:
                    to_del = to_check
                elif comp_course[1] < to_check[1]:
                    to_del = (comp_course[0], comp_course[1])

    if to_del != 0:
        students[name].remove(to_del)   

def summary(students):
    print(f"students {len(students)}")
    count = 0
    name = ""
    for student, courses in students.items():
        if len(courses) > count:
            count = len(courses)
            name = student
    print(f"most courses completed {count} {name}")
    grade = 0
    count = 0
    name = ""
    for student, courses in students.items():
        temp = 0
        for course in courses:
            temp += course[1]
        temp2 = temp/len(courses)
        if temp2 > grade:
            grade = temp2
            name = student
    print(f"best average grade {grade} {name}")
            
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Advanced Course in Programming", 3))
    print_student(students, "Peter")