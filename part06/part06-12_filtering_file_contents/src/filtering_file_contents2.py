import operator

ops = { "+": operator.add, "-": operator.sub }

def filter_solutions():
    with open("solutions.csv") as file1, open("correct.csv", "w") as file2, open("incorrect.csv", "w") as file3:
        for line in file1:
            parts = line.split(";")
            parts[2] = int(parts[2])
            str_equation = parts[1]
            operand_list = [int(str_equation[0]), int(str_equation[2])]
            if ops[str_equation[1]](operand_list[0],operand_list[0]) == parts[2]:
                file2.write(line+"\n")
            else:
                file3.write(line+"\n")