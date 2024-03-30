import random
print("добро пожаловать в игру камень ножницы бумага!")
count = int(input("Cколько раз хочешь играть?\n"))
playerScore=0
botScore=0
print("камень - 1 \nножницы - 2\nбумага - 3 \nящерица - 4\nспок - 5 \n")
    
for i in range(count):
    answer = input("Что выберешь?\n").lower()
    if answer.find("1") != -1:
        answer = "к"
    elif answer.find("2") != -1: 
        answer = "н"
    elif answer.find("3") != -1: 
        answer = "б"
    if answer.find("4") != -1:
        answer = "я"
    elif answer.find("5") != -1:
        answer = "с"
    botAnswer = random.choice(["камень", "ножницы", "бумагу", "ящерица", "спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    print(botAnswer)
    if answer == botAnswer:
        print("ничья!")
    elif (answer == "н" and botAnswer == "б") or\
        (answer == "б" and botAnswer == "к") or \
        (answer == "к" and botAnswer == "я") or\
        (answer == "я" and botAnswer == "с") or \
        (answer == "с" and botAnswer == "н")or\
        (answer == "н" and botAnswer == "я") or \
        (answer == "я" and botAnswer == "б")or\
        (answer == "б" and botAnswer == "с") or \
        (answer == "с" and botAnswer == "к") or \
        (answer == "к" and botAnswer == "н"):
        print("ты победил!")
        playerScore+=1
    else:
        print("я победил!")
        botScore+=1
if playerScore == botScore:
    print(f"ничья по итогам {count} раундов!")
elif playerScore > botScore:
    print(f"ты победил по итогам {count} раундов")
else: print(f"я победил по итогам {count} раундов")