def add_student(students: dict, name: str):
    if name not in students:
        students[name] = "no completed courses"
    
def print_student(students: dict, name: str):
    if name in students and students[name] == "no completed courses":
        print(f"{name}:\n {students[name]}")
    
    elif name in students and students[name] != "no completed courses":
        list1 = students[name]
        print(f"{name}:\n {len(list1)} completed courses:")
        sum_grade = 0 
        for index in list1:
            print(f"  {index[0]} {index[1]}")
            sum_grade += index[1]
        print(f" average grade {sum_grade/len(list1)}")    
    
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, tuple: tuple):
    
    if name in students and students[name] == "no completed courses" and tuple[1] != 0:
        students[name] = []
        students[name].append(tuple)
    
      
    elif tuple[1] != 0:
        students[name].append(tuple) 
        i = 0 
        for key,value in students.items():
            if name == key:
                if value[i][0] == tuple[0] and tuple[1] < value[i][1]:
                    students[name].pop()
                    break
                elif value[i][0] == tuple[0] and tuple[1] > value[i][1]:
                    students[name].pop(i)
                    
                    break
                i += 1
                    

def summary(students: dict):
    
    length = []
    values = []
    grades = []
    avg_grade = []
    a = 0    
    
    for key,value in students.items():
        length.append(len(value))
        
    for x in length:
        if x > a:
            a = x
            
    print(f"students {len(students)}")
    for key,value in students.items():
        if len(value) == a:
            print(f"most courses completed {len(value)} {key}")
       
    for value in students.values():
        values.append(value)
        
    for list1 in values:
        for tuple1 in list1: 
            grades.append(tuple1[1])
    
    c = 0
    d= 0
    r = 0
    x= 0
    for t in length:
        b = 0
        for s in range(d, d + t):
            b += grades[s]
            d += 1
            r += 1
            if r == length[x]:
                c = b / t
                avg_grade.append(c)
                x += 1
                r = 0
    
    e = 0
    for biggest in avg_grade:
        if biggest > e:
            e = biggest
    
    g = avg_grade.index(e)
                        
    for key,value in students.items():
        if len(value) == length[g]:
            print(f"best average grade {avg_grade[g]} {key}")
        
           
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Advanced Course in Programming", 3))
    print_student(students, "Peter")