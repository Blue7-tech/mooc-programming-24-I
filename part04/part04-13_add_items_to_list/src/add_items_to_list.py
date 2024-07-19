# Write your solution here

i = int(input("How many items:"))
k = 1

numbers = []

while i > 0:
    item = int(input(f"Item {k}:"))
    numbers.append(item)
    i -= 1
    k += 1

print(numbers)