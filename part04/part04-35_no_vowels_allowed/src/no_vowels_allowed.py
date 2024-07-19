# Write your solution here

def no_vowels(my_string):
    no_vowels = ""
    for i in my_string: 
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            continue
        no_vowels += i
        
    return no_vowels

    
if __name__ == "__main__":     
    my_string = "this is an example"
    print(no_vowels(my_string))