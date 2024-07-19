# Write your solution here

def longest(strings: list):
    len_strings = []
    for i in strings:
        len_strings.append(len(i))
        
    count = 0
    for i in len_strings:
        count += 1
        if i == max(len_strings):
            break
    
    index = count - 1
    return strings[index]      

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
