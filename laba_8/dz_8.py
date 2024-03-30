import random
string = input("Введите строку\n").lower()
wodr = input("Введите слово\n").lower()
if string.find(wodr) != -1:
    x = string.find(wodr)
    print(f"нашли слово! на позиции {x}")  