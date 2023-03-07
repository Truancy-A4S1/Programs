import turtle

turt=turtle.Turtle()

screen_color = turtle.Screen()
screen_color.bgcolor('black')

turt.pencolor('green')

a=0
b=0

for i in range(100):
    turt.forward(a)
    turt.right(b)
    a+=10
    b+=4
    turt.hideturtle()

turtle.done()