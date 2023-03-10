from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed('fastest')
color_list = ['red', 'green', 'blue', 'orange', 'black',
              'yellow', 'brown', 'purple', 'pink', 'gold', 'silver', "gray"]
timmy_the_turtle.pu()
timmy_the_turtle.right(90)
timmy_the_turtle.forward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(200)
timmy_the_turtle.right(180)
timmy_the_turtle.pd()
for turt in range(10):
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.pu()
    timmy_the_turtle.forward(50)
    timmy_the_turtle.pd()


screen = Screen()
screen.exitonclick()
