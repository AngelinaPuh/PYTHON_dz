import turtle
turtle.shape("turtle")
turtle.speed(5)
angle = int(input("введите количество углов"))
size = int(input("введите длину стороны"))
if angle < 5:
 print("углов не может быть меньше пяти")
elif angle == 5:
 turtle.forward(size)
 turtle.left(120)
 turtle.forward(size)
 turtle.left(120)
 turtle.forward(size)
elif angle == 6:
 turtle.forward(size)
 turtle.left(90)
 turtle.forward(size)
 turtle.left(90)
 turtle.forward(size)
 turtle.left(90)
 turtle.forward(size)
 turtle.exitonclick()