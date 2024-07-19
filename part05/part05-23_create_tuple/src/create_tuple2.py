def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    biggest = max(x, y, z)
    test = x+y+z

    return smallest, biggest, test

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
