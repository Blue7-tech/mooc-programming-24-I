# Write your solution here
def hash_square(length):
    star = "#"
    i = 0
    while i < length:
        print(star * length)
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)