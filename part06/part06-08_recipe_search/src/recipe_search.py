# Write your solution here
def get_words(filename):
    recipe_list = []    
    with open(filename) as file:
        recipe = []
        for line in file:
            if line == "\n":
                recipe_list.append(recipe)
                recipe = []
                continue
            recipe.append(line.strip())
        recipe_list.append(recipe)
        
    for recipe in recipe_list:
        recipe[1] = int(recipe[1])
            
    return recipe_list    

def search_by_name(filename: str, word: str):
    result = []
    recipe_list = get_words(filename)
    for recipe in recipe_list:
        if word in recipe[0].lower():
            result.append(recipe[0])
    
    return result
    
def search_by_time(filename: str, prep_time: int):
    result = []
    recipe_list = get_words(filename)
    for recipe in recipe_list:
        if prep_time >= recipe[1]:
            result.append((recipe[0], recipe[1]))
    
    result_formated = []
    for combination in result:
       result_formated.append(f"{combination[0]}, preparation time {combination[1]} min") 
    
    return result_formated

def search_by_ingredient(filename: str, ingredient: str):
    result = []
    recipe_list = get_words(filename)
    for recipe in recipe_list:
        if ingredient in recipe[2:]:
           result.append((recipe[0], recipe[1]))
    
    result_formated = []
    for combination in result:
       result_formated.append(f"{combination[0]}, preparation time {combination[1]} min") 
    
    return result_formated
    

if __name__ == "__main__":
    print(get_words("recipes1.txt"))
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)