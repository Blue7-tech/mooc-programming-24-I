def filter_incorrect():
    with open("lottery_numbers.csv") as file1, open("correct_numbers.csv", "w") as file2:
        for line in file1:
            parts = line.split(",")
            temp = parts[0].split(";")
            parts[0] = temp[1]
            parts.insert(0, temp[0])
            if len(parts) != 8:
                continue          
            try:
                int(parts[0][5:])
                check = []
                for i in range(1,len(parts)):
                    temp = int(parts[i])
                    if temp < 1 or temp > 39:
                        raise ValueError
                    if temp in check:
                        raise ValueError
                    check.append(temp)           
            except ValueError:
                continue
            file2.write(line)
            
filter_incorrect()