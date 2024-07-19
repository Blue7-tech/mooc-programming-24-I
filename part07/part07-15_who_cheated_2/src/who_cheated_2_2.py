
from datetime import datetime
from datetime import timedelta
import csv  

def final_points():
    student_final_points_nested = {}
    student_start_time = {}
    final_points = {}
    with open("start_times.csv") as file1, open("submissions.csv") as file2:
        for line in csv.reader(file1, delimiter=";"):
            name = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")
            student_start_time[name] = start_time
            student_final_points_nested[name] = {}
            
        for line in csv.reader(file2, delimiter=";"):
            name = line[0]
            task = int(line[1])
            points = int(line[2])
            submission_time = datetime.strptime(line[3], "%H:%M")
            if submission_time - student_start_time[name] < timedelta(hours=3):
                student_final_points_nested[name][task] = points
    
        
    with open("submissions.csv") as file2:
        for line in csv.reader(file2, delimiter=";"):
            name = line[0]
            task = int(line[1])
            points = int(line[2])
            submission_time = datetime.strptime(line[3], "%H:%M")
            if submission_time - student_start_time[name] < timedelta(hours=3) and points > student_final_points_nested[name][task]:
                student_final_points_nested[name][task] = points
      
    
    temp = 0
    for name, dictionary in student_final_points_nested.items():
        for points in dictionary.values():
            temp += points
        final_points[name] = temp
        temp = 0
        
    return final_points
        
if __name__ == "__main__":
    print(final_points())