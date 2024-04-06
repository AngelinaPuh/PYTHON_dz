import random
while True:
    answer = input("Задайте вопрос: \n").lower()
    botAnswer = random.choice(["да", "нет", "мб"])
    print(f"{botAnswer}")
    next = input("хотите попробовать ещё раз?")
    if next.lower() != "да" :
        break
print(f"приходите еще)")