print("What is the weather forecast tomorrow?")
temperature = int(input("Temperature:"))
rain = input("Will it rain (yes/no):")

if temperature > 20:
    print("Wear jeans and a T-shirt")
    if rain == "yes":
        print("Don't forget your umbrella!")      
            
elif temperature > 10:
    print("""Wear jeans and a T-shirt
I recommend a jumper as well""")
    if rain == "yes":
            print("Don't forget your umbrella!")  
    
elif temperature > 5:
    print("""Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you""")
    if rain == "yes":
            print("Don't forget your umbrella!")  
    
else:
    print("""Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order""")
    if rain == "yes":
            print("Don't forget your umbrella!") 
    
