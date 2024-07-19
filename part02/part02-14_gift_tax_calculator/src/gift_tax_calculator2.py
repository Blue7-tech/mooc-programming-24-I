value = int(input("Value of gift: "))

if 5000 <= value < 25000:
    tax = 100
    tax_rate = 0.08 
    print(f"Amount of tax: {tax + (value - 5000) * tax_rate:.5f} euros")

elif 25000 <= value < 55000:
    tax = 1700
    tax_rate = 0.1
    print(f"Amount of tax: {tax + (value - 25000) * tax_rate} euros")

elif 55000 <= value < 200000:
    tax = 4700
    tax_rate = 0.12
    print(f"Amount of tax: {tax + (value - 55000) * tax_rate}. euros")
    
elif 200000 <= value < 1000000:
    tax = 22100
    tax_rate = 0.15
    print(f"Amount of tax: {(tax + (value - 200000) * tax_rate):.1f} euros")

elif value >= 1000000:
    tax = 142100
    tax_rate = 0.17
    print(f"Amount of tax: {tax + (value - 1000000) * tax_rate} euros")

else:
    print("No tax!")