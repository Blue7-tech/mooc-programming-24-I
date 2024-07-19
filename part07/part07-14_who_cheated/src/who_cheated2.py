

# Write your solution here

from datetime import datetime
from datetime import timedelta
import csv  


def cheaters():
    cheater_list = []
    student_start_time = {}
    with open("start_times.csv") as file1, open("submissions.csv") as file2:
        for line in csv.reader(file1, delimiter=";"):
            name = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")
            student_start_time[name] = start_time

        for line in csv.reader(file2, delimiter=";"):
            name = line[0]
            submission_time = datetime.strptime(line[3], "%H:%M")
            if name in student_start_time and name not in cheater_list and submission_time - student_start_time[name] > timedelta(hours=3):
                cheater_list.append(name)
        
        return student_start_time
                    
if __name__ == "__main__":
    print(cheaters())