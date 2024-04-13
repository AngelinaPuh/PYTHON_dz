answer = float(input("Введите массу конфет в граммах: \n"))
kg = answer/1000
if answer > 2000:
    price = kg*200
    print(f" Цена за кг равна 200 рублей ") 
else:
    price = kg*250
    print(f" Цена за кг равна 250 рублей ") 
print(f" Цена равна {price} рублей") 

