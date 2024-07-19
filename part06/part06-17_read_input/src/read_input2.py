def read_input(characters: str, number1: int, number2: int):
    while True:
        try:
            input_user = int(input(characters))
            if input_user >= number1 and input_user <= number2:
                return input_user
            else:
                print("You must type in an integer between 5 and 10")
        
        except ValueError:
            print("You must type in an integer between 5 and 10")


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)