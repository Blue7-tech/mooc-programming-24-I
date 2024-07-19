# Write your solution here
from datetime import datetime, timedelta

def final_points():
    with open("start_times.csv") as file1, open("submissions.csv") as file2:
        students_start_time = {}
        for line in file1:
            line = line.strip()
            parts = line.split(";")
            start_time = datetime.strptime(parts[1], "%H:%M")
            students_start_time[parts[0]] = start_time
        
        students_sub = {}
        for line in file2:
            line = line.strip()
            parts = line.split(";")
            parts[1] = int(parts[1])
            parts[2] = int(parts[2])
            sub_time = datetime.strptime(parts[3], "%H:%M")
            if sub_time - students_start_time[parts[0]] > timedelta(hours = 3):
                continue
            if parts[0] not in students_sub:
                students_sub[parts[0]] = {parts[1]: parts[2]}
            elif parts[0] in students_sub:
                if parts[1] in students_sub[parts[0]]:
                    if parts[2] > students_sub[parts[0]][parts[1]]:
                        students_sub[parts[0]][parts[1]] = parts[2]
                else:
                    students_sub[parts[0]][parts[1]] = parts[2]
        
        students_result = {}            
        for key, value in students_sub.items():
            total_points = 0
            for key2, value2 in value.items():
                total_points += value2
            students_result[key] = total_points
                   
        return students_result
        
if __name__ == "__main__":
    print(final_points())


