# Write your solution here
def anagrams(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(anagrams("tame", "meta"))