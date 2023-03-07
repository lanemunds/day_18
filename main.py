from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
color_list = ['red', 'green', 'blue', 'orange', 'black',
              'yellow', 'brown', 'purple', 'pink', 'gold', 'silver', "gray"]
timmy_the_turtle.width(5)

timmy_the_turtle.color(random.choice(color_list))
for turt in range(3):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(120)


timmy_the_turtle.color(random.choice(color_list))
for turt in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.color(random.choice(color_list))
for turt in range(5):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(72)

timmy_the_turtle.color(random.choice(color_list))
for turt in range(6):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(60)

timmy_the_turtle.color(random.choice(color_list))
for turt in range(7):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(51.428)

timmy_the_turtle.color(random.choice(color_list))
for turt in range(8):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(45)

screen = Screen()
screen.exitonclick()
