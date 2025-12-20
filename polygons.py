from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


for x in range(3,11):
    for y in range(x):
        tim.forward(50)
        tim.right(360/x)
        
screen.exitonclick()