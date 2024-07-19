# Write your solution here

def list_sum(list1, list2):
    list = []
    i = 1
    k = 0
    while i <= len(list1):
        list.append(list1[k] + list2[k])
        i += 1
        k += 1 
    return list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))