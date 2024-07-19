def dict_of_numbers():
    result = {}
    for i in range(100):
        result[i] = ""

    numbers_in_tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    merged = []
    
    merged.append("zero")
    for number in numbers:
        merged.append(number)
    merged.append("ten")
    merged.append("eleven")
    merged.append("twelve")
    merged.append("thirteen")
    merged.append("fourteen")
    merged.append("fifteen")
    merged.append("sixteen")
    merged.append("seventeen")
    merged.append("eighteen")
    merged.append("nineteen")

    
    for tens_number in numbers_in_tens:
        merged.append(tens_number)
        for number in numbers:
            temp = tens_number + "-" + number
            merged.append(temp)
    
    for i in range(100):
        result[i] = merged[i]
    return result
    
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])