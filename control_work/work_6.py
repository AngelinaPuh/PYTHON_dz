import turtle
turtle.shape("turtle")
turtle.speed(1000)
num = int(input('Радиус круга '))
turtle.pensize(5)
colors = ["blue", "orange", "green", "red"]
for i in range(4): 
    turtle.color(colors[i])
    turtle.circle(num)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20) 
    turtle.left(90)
    turtle.pendown()
    num = num + 20 
turtle.exitonclick() 