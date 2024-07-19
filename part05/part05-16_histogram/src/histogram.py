# Write your solution here
def histogram(string:str):
    histogram = {}
    
    for letter in string:
        if letter not in histogram:
            histogram[letter] = []
        histogram[letter].append("*")
    
    for key,value in histogram.items():
        star = ""
        for item in value:
            star += item    
        print(f"{key} {star}")
        
if __name__ == "__main__":
    histogram("statistically")