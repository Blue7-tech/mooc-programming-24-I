# Write your solution here

def store_personal_data(person: tuple):
   
    string_element =""
    for data in person:
        string_element += str(data) + ";"
    string_element = string_element[:len(string_element)-1]
    
    with open("people.csv", "a") as my_file:
        my_file.write(string_element + "\n")
        
if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))