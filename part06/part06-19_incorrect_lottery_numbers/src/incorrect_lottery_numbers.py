# Write your solution here

def filter_incorrect():
    with open("lottery_numbers.csv") as source, open("correct_numbers.csv", "w") as correct_file:
        for line in source:
            line = line.replace("\n", "")
            parts = line.split(";")
            header = parts[0]
            string_numbers = parts[1]
            header_list = header.split(" ")
            week = header_list[0]
            try:
                week_number = int(header_list[1])
            except:
                continue
           
            integer_numbers_list = []
            string_numbers_list = string_numbers.split(",")
            for number in string_numbers_list:
                try:
                    integer_numbers_list.append(int(number))
                except:
                    continue
            
            integer_numbers_list_correct = []
            for number in integer_numbers_list:
                if 1 <= number <= 39:
                    integer_numbers_list_correct.append(number)
                
            if len(integer_numbers_list_correct) != 7:
                continue
            
            temp = []
            for number in integer_numbers_list_correct:
                if number in temp:
                    break
                temp.append(number)
            
            if len(temp) != 7:
                continue    
            
            correct_file.write(line + "\n")
      
if __name__ == "__main__":
    filter_incorrect()