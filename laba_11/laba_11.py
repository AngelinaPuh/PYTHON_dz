from turtle import *
from random import randint
shape("turtle")
colors = ["blue", "red", "orange", "purple"]
shredder = randint(1,10)
user_choose = 0

while user_choose != shredder:
    user_choose = str.lower(input("выберите направление влево/вправо/вперед/назад - "))
    if user_choose == str.lower("влево"):
        left(90)
        for color_turtle in colors:
            pensize(randint(1,10))
            color(color_turtle)
            forward(randint(5,30))
        user_choose = randint(1,10)
        if user_choose!= shredder:
            print("Shredder здесь нет, идем дальше")
    elif user_choose == str.lower("вправо"):
        right(90)
        for color_turtle in colors:
            pensize(randint(1,10))
            color(color_turtle)
            forward(randint(5,30))
        user_choose = randint(1,10)
        if user_choose!= shredder:
            print("Shredder здесь нет, идем дальше")
    elif user_choose == str.lower("вперед"):
        for color_turtle in colors:
            pensize(randint(1,10))
            color(color_turtle)
            forward(randint(5,30))
        user_choose = randint(1,10)
        if user_choose!= shredder:
            print("Shredder здесь нет, идем дальше")
    elif user_choose == str.lower("назад"):
        left(180)
        for color_turtle in colors:
            pensize(randint(1,10))
            color(color_turtle)
            forward(randint(5,30))
        user_choose = randint(1,10)
        if user_choose!= shredder:
            print("Shredder здесь нет, идем дальше")
print("Shredder here!")   