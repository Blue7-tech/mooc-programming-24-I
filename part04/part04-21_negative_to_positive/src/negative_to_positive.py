# Write your solution here

pos_int = int(input("Please type in a positive integer:"))

for x in range(-pos_int, pos_int+1, 1):
    if x == 0:
        continue
    print(x)
    
