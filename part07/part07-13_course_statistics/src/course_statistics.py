# Write your solution here
import urllib.request 
import json
import math
def retrieve_all():
    data = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(data.read())    
    
    count = 0
    courses_enabled = []
    for course in courses:
        for exercise in course["exercises"]:
            count += exercise
        course["exercises"] = count
        count = 0
        if course["enabled"]:
            courses_enabled.append(course)
    
    list_result = []     
    for course in courses_enabled:
        temp = (course["fullName"], course["name"], course["year"], course["exercises"])
        list_result.append(temp)
        
            
    return list_result

def retrieve_course(course_name: str):
    data = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2020/stats")
    course = json.loads(data.read())      
    
    course_dict = {
    "weeks": len(course),
    "students": 0,
    "hours": 0,
    "hours_average": 0,
    "exercises": 0,
    "exercises_average": 0 
    } 
    
    i = 0
    for key, value in course.items():
        if i == 0:
            course_dict["students"] += value["students"]
        course_dict["hours"] += value["hour_total"]
        course_dict["hours_average"] += value["hour_total"] / course_dict["students"]
        course_dict["exercises"] += value["exercise_total"]
        course_dict["exercises_average"] += value["exercise_total"] / course_dict["students"]
        i += 1
    
    course_dict["hours_average"] = math.floor(course_dict["hours_average"])
    course_dict["exercises_average"] = math.floor(course_dict["exercises_average"])
    
    return course_dict
    
if __name__ == "__main__":
    print(retrieve_course("docker2020"))

