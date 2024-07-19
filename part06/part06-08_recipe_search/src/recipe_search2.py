def search_by_name(filename: str, word: str):
    content = []
    with open(filename) as file:
        for line in file:
            content.append(line.strip())
    
    content_int = []
    temp = 0
    start = False
    for i in range(0,len(content)):
        if i == 1:
            content_int.append(int(content[i]))
            start = True
        elif content[i] == "":
            content_int.append(content[i])
            temp = i + 2
        elif start and i == temp:
            content_int.append(int(content[i]))
            temp = 0
        else:
            content_int.append(content[i])
    
    recipes = {}    
    start = False
    for i in range(0,len(content_int)):
        if i == 0:
            a = i
            recipes[content_int[a]] = []
            continue
        elif content_int[i] == "":
            a = i + 1
            start = True
            continue
        elif start and i == a:
            recipes[content_int[a]] = []
            continue
        recipes[content_int[a]].append(content_int[i])
    
    result = []
    for key in recipes.keys():
        if word in key.lower():
            result.append(key)
    
    return result                   

def search_by_time(filename: str, prep_time: int):
    content = []
    with open(filename) as file:
        for line in file:
            content.append(line.strip())
    
    content_int = []
    temp = 0
    start = False
    for i in range(0,len(content)):
        if i == 1:
            content_int.append(int(content[i]))
            start = True
        elif content[i] == "":
            content_int.append(content[i])
            temp = i + 2
        elif start and i == temp:
            content_int.append(int(content[i]))
            temp = 0
        else:
            content_int.append(content[i])
    
    recipes = {}    
    start = False
    for i in range(0,len(content_int)):
        if i == 0:
            a = i
            recipes[content_int[a]] = []
            continue
        elif content_int[i] == "":
            a = i + 1
            start = True
            continue
        elif start and i == a:
            recipes[content_int[a]] = []
            continue
        recipes[content_int[a]].append(content_int[i])
    
    result = []
    for key,value in recipes.items():
        if value[0] <= prep_time:
            temp = f", preparation time {value[0]} min"
            final = key + temp
            result.append(final)
    
    return result           

def search_by_ingredient(filename: str, ingredient: str):
    content = []
    with open(filename) as file:
        for line in file:
            content.append(line.strip())
    
    content_int = []
    temp = 0
    start = False
    for i in range(0,len(content)):
        if i == 1:
            content_int.append(int(content[i]))
            start = True
        elif content[i] == "":
            content_int.append(content[i])
            temp = i + 2
        elif start and i == temp:
            content_int.append(int(content[i]))
            temp = 0
        else:
            content_int.append(content[i])
    
    recipes = {}    
    start = False
    for i in range(0,len(content_int)):
        if i == 0:
            a = i
            recipes[content_int[a]] = []
            continue
        elif content_int[i] == "":
            a = i + 1
            start = True
            continue
        elif start and i == a:
            recipes[content_int[a]] = []
            continue
        recipes[content_int[a]].append(content_int[i])
    
    result = []
    for key,value in recipes.items():
        if ingredient in value:
            temp = f", preparation time {value[0]} min"
            final = key + temp
            result.append(final)
    
    return result         
       
if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)