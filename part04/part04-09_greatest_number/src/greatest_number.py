# Write your solution here
def greatest_number(x, y, z):
    if x > y and x > z:
        return x
    elif y >  x and y > z:
        return y
    elif z > x and z > y:
        return z      
    elif x == z or x == y:
        return x 
    elif z == y:
        return z


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)