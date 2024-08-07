from turtle import *

turtle = Turtle()
turtle.color("red")

for i in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()