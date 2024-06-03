from turtle import *

bgcolor("white")
speed(0)
hideturtle()

for i in range(2220):
    color("red")
    circle(i)
    color("green")
    circle(i*0.8)
    right(3)
    forward(3)

done()