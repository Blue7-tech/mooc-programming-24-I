import string
import operator
alphabet = string.ascii_uppercase

def run(commands: list):
    variables = {}
    locations = {}
    
    results = []
    operators = {"<=": operator.le, "==": operator.eq, "<": operator.lt, ">": operator.gt, ">=": operator.ge}
    
    for i in range(len(commands)):
        if ":" in commands[i]:
            temp = commands[i][:-1] 
            locations[temp] = i
    
    i = 0
    while i < len(commands):
        temp = commands[i].split(" ")       
        if temp[0] == "MOV":
            if temp[2] not in alphabet:
                temp[2] = int(temp[2])
                variables[temp[1]] = temp[2] 
            elif temp[2] in alphabet:
                variables[temp[1]] = variables[temp[2]]
        elif temp[0] == "PRINT":
            if temp[1] in alphabet:
                results.append(variables[temp[1]])
            elif temp[1] not in alphabet:
                temp[1] = int(temp[1])
                results.append(temp[1])
        elif temp[0] == "ADD":
            if temp[2] in alphabet:   
                variables[temp[1]] += variables[temp[2]]
            elif temp[2] not in alphabet:
                temp[2] = int(temp[2])
                variables[temp[1]] += temp[2]
        elif temp[0] == "END":
            break 
        elif temp[0] == "IF":
            if temp[3] in alphabet:
                if operators[temp[2]](variables[temp[1]],variables[temp[3]]):
                    i = locations[temp[5]]
            elif temp[3] not in alphabet:
                temp[3] = int(temp[3])
                if operators[temp[2]](variables[temp[1]],temp[3]):
                    i = locations[temp[5]]
        elif temp[0] == "JUMP":
            i = locations[temp[1]]
        elif temp[0] == "MUL":
            if temp[2] in alphabet:   
                variables[temp[1]] *= variables[temp[2]]
            elif temp[2] not in alphabet:
                temp[2] = int(temp[2])
                variables[temp[1]] *= temp[2]
        elif temp[0] == "SUB":
            if temp[2] in alphabet:   
                variables[temp[1]] -= variables[temp[2]]
            elif temp[2] not in alphabet:
                temp[2] = int(temp[2])
                variables[temp[1]] -= temp[2]    

        i += 1
    
    return results

if __name__ == "__main__":
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)