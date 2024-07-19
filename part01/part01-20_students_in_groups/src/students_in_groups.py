# Write your solution here
number = int(input("How many students on the course?"))
group_size = int(input("Desired grouzp size?"))
number_groups = number // group_size

if number / group_size != number // group_size:
    number_groups += 1
    print(f"Number of groups formed: {number_groups}")
    
else:
    print(f"Number of groups formed: {number_groups}")