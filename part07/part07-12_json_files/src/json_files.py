# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        py_data = json.loads(data)
    
    for student in py_data:
        print(f"{student["name"]} {student["age"]} years", end = "")
        temp = ""
        for hobby in student["hobbies"]:
            temp += hobby + ", "
        temp = temp.strip()
        temp = temp[:-1]
        print(f" ({temp})")
    
    
if __name__ == "__main__":
    print_persons("file1.json")
    