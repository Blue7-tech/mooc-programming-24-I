# Write your solution here

def dict_of_numbers():
    # creating list with written numbers
    word_number = []
    first_word = []
    first_word.append("twenty")
    first_word.append("thirty")
    first_word.append("forty")
    first_word.append("fifty")
    first_word.append("sixty")
    first_word.append("seventy")
    first_word.append("eighty")
    first_word.append("ninety")
    i = 0
    j = 0
    k = 0
    temp = ""
    second_word = ["-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine"]  
    for item in second_word:
        if i == 0 or i == 9 or i == 18 or i == 27 or i == 36 or i == 45 or i == 54 or i == 63:
            word_number.append(first_word[k])
            k += 1
        if i == 9 or i == 18 or i == 27 or i == 36 or i == 45 or i == 54 or i == 63:
            j += 1    
        temp = first_word[j] + item
        word_number.append(temp)
        i += 1
    
    remainder = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    remainder.reverse()
    
    for item in remainder:
        word_number.insert(0,item)   
    
    # creating the dictionary
    dict_of_numbers = {}
    i=0
    while i < 100:
        dict_of_numbers[i] = 0
        i += 1

    i = 0
    for key in dict_of_numbers.keys():
        dict_of_numbers[key] = word_number[i]
        i += 1    
    
    return dict_of_numbers
    
    """word_number = []
    first_word = []
    first_word.append("twenty")
    first_word.append("thirty")
    first_word.append("fourty")
    first_word.append("fifty")
    first_word.append("sixty")
    first_word.append("seventy")
    first_word.append("eighty")
    first_word.append("ninety")
    i = 1
    j = 0
    temp = ""
    second_word = ["-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine",
                   "-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine"]  
    for item in second_word:
        
        if i == 10 or i == 19 or i == 28 or i == 37 or i == 46 or i == 55 or i == 64:
            j += 1    
        temp = first_word[j] + item
        word_number.append(temp)
        i += 1
    
    i=0
    for item in first_word:
        word_number.insert(i,item)
        i += 10"""
    
    """twenties = []
    twenties.insert(0,"twenty")
    twenties_index0 = "twenty"
    temp = ""
    second_word = ["-one","-two","-three","-four","-five", "-six", "-seven", "-eight", "-nine"]  
    for item in second_word:
        temp = twenties_index0 + item
        twenties.append(temp)
    
    i = 20
    for item in twenties:
        dict_of_numbers[i] = item
        i += 1"""

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])