def anagrams(string1, string2):
    my_list = [string1, string2]
    
    result = []
    for item in my_list:
        result.append(sorted(item))
        
    return result[0] == result[1]


if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False