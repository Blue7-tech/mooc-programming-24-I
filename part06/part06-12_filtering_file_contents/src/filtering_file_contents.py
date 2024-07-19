# Write your solution here

def check_results():
    test = []
    with open("solutions.csv") as solutions_file:
        for line in solutions_file:
            line = line.replace("\n", "")
            if "+" in line:
                line = line.replace("+", " ")
            elif "-" in line:
                line = line.replace("-", " ")
            parts = line.split(";")
            integer = 2
            integer2 = 1
            for i in range(0,len(parts)):
                if i == integer:
                     test.append(int(parts[i]))
                     integer += 3
                     continue
                if i == integer2:
                    a = parts[i].split(" ")
                    for number in a:
                        test.append(int(number))
                    integer2 += 3
                    continue
                test.append(parts[i])
    
        
    test2 = []
    start = 1
    numb1 = 0
    numb2 = 0
    for i in range(0, len(test)):
            if test[i] == str:
                continue
            elif i == start:
                numb1 = test[i] 
            elif i == start + 1:
                numb2 = test[i]
            elif i == start + 2:
                if numb1 + numb2 == test[i]:
                    x = 1
                    test2.append(x)
                    start += 4
                elif numb1 - numb2 == test[i]:
                    x = 1
                    test2.append(x)
                    start += 4
                else:
                    x = 0
                    test2.append(x)
                    start += 4
    
    return test2
    
    a = 0
    b = 3
    students = []
    for item in test2:
        students.append(test[a])
        students.append(test[b])
        students.append(item)
        a += 4
        b += 4
    
    
    
    index0 = 0
    index1 = 1
    index2 = 2
    end = int(len(students)/3)
    results = []
    for i in range(0, end):
        temp = []
        temp.append(students[index0])
        temp.append(students[index1])
        temp.append(students[index2])
        results.append(temp)
        index0 += 3
        index1 += 3
        index2 += 3  
    
    

def filter_solutions():
    results = check_results()
    
    with open("solutions.csv") as solutions_file:
        
        with open("correct.csv", "w") as correct_file:
            
            with open("incorrect.csv", "w") as incorrect_file:
                index = 0
                for line in solutions_file:
                    for i in range(len(results)):
                        if results[index] == 1:
                            correct_file.write(line)
                            index += 1
                            break
                        elif results[index] == 0:
                            incorrect_file.write(line)
                            index += 1
                            break
                                
if __name__ == "__main__":                        
    filter_solutions()