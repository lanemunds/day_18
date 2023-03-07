from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.width(15)
timmy_the_turtle.speed('fastest')
color_list = ['red', 'green', 'blue', 'orange', 'black',
              'yellow', 'brown', 'purple', 'pink', 'gold', 'silver', "gray"]
distance = 40
angle = [0, 90, 180, 270]


def randWalk(num):
    for turt in range(num):
        timmy_the_turtle.color(random.choice(color_list))
        timmy_the_turtle.setheading(random.choice(angle))
        timmy_the_turtle.forward(distance)


randWalk(100)


screen = Screen()
screen.exitonclick()
