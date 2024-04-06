import turtle
answer = int(input("Введите длину сторону квадрата "))
half = answer/2

turtle.shape("turtle")
# поднять перо
turtle.penup()
turtle.left(180)
turtle.forward(half)
turtle.left(180)
# опустить перо
turtle.pendown()
for i in range(4): 
    turtle.forward(answer) 
    turtle.left(90)
turtle.exitonclick()