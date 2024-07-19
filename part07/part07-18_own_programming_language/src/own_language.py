# Write your solution here
import string
import operator

def run(program:list):
    
    upper_case_letter = string.ascii_uppercase
    result = []
    variables = {}
    locations = {}
    operators = {
        "==" : operator.eq,
        "!=" : operator.ne,
        "<" : operator.lt,
        "<=" : operator.le,
        ">" : operator.gt,
        ">=" : operator.ge
    }
    
    for i in upper_case_letter:
        variables[i] = 0
    
    # pre iteration of the command list to get all indices for the locatios
    for i in range(len(program)):
        temp = program[i].split(" ")
        if ":" in temp[0]:
            locations[temp[0][:-1]] = program.index(temp[0])
    
    # main iteration of the command list
    i = 0
    while i < len(program):
        temp = program[i].split(" ")
        # move command sets variable and value in dictionary, both cases not to included for int and variable
        if temp[0] == "MOV" and temp[2] not in upper_case_letter:
            variables[temp[1]] = int(temp[2])  
        elif temp[0] == "MOV":
            variables[temp[1]] = variables[temp[2]]         
        # print command appends variable's referenced value in final list or appends value without variable to final list
        elif temp[0] == "PRINT" and temp[1] not in upper_case_letter:
            result.append(int(temp[1]))
        elif temp[0] == "PRINT":
            result.append(variables[temp[1]])
        # add command adds value to existing variable, by value referenced from other variable or only value
        elif temp[0] == "ADD" and temp[2] not in upper_case_letter:
            variables[temp[1]] += int(temp[2])
        elif temp[0] == "ADD" :
            variables[temp[1]] += variables[temp[2]]
        # sub command subtracts value to existing variable, by value referenced from other variable or only value
        elif temp[0] == "SUB" and temp[2] not in upper_case_letter:
            variables[temp[1]] -= int(temp[2])
        elif temp[0] == "SUB":
            variables[temp[1]] -= variables[temp[2]]
        # mul command multiplies value to existing variable, by value referenced from other variable or only value
        elif temp[0] == "MUL" and temp[2] not in upper_case_letter:
            variables[temp[1]] *= int(temp[2]) 
        elif temp[0] == "MUL":
            variables[temp[1]] *= variables[temp[2]]
        # jump command directly influece variable i in while loop. while loop iteration is getting modified    
        elif temp[0] == "JUMP":
            i = locations[temp[1]]
        # conditional statement, if true the while loop iteration is getting modified by indices from location dictionary, direct influece on i in while loop
        elif temp[0] == "IF" and temp[3] not in upper_case_letter: 
            if operators[temp[2]](variables[temp[1]], int(temp[3])):
                i = locations[temp[5]]
        elif temp[0] == "IF": 
            if operators[temp[2]](variables[temp[1]], variables[temp[3]]):
                i = locations[temp[5]]       
        # end command stops iteration
        elif temp[0] == "END":
            break       
        i +=1 
            
    return result

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)