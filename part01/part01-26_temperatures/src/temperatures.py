temperatureF = int(input("Please type in a temperature (F):"))
temperatureC = (temperatureF - 32) * 5/9

if temperatureC < 0:
    print(f"""{temperatureF} degrees Fahrenheit equals {temperatureC} degrees Celsius
Brr! It's cold in here!""")

else:
    print(f"{temperatureF} degrees Fahrenheit equals {temperatureC} degrees Celsius")