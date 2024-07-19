from datetime import datetime, timedelta

def cheaters():
    with open("start_times.csv") as file1, open("submissions.csv") as file2:
        students_start_time = {}
        for line in file1:
            line = line.strip()
            parts = line.split(";")
            start_time = datetime.strptime(parts[1], "%H:%M")
            students_start_time[parts[0]] = start_time
        
        cheaters = []
        for line in file2:
            line = line.strip()
            parts = line.split(";")
            parts[1] = int(parts[1])
            parts[2] = int(parts[2])
            sub_time = datetime.strptime(parts[3], "%H:%M")
            if sub_time - students_start_time[parts[0]] > timedelta(hours = 3):
                if parts[0] not in cheaters:
                    cheaters.append(parts[0])
            
        return cheaters

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

        print(students_sub)
        
if __name__ == "__main__":
    print(cheaters())
    