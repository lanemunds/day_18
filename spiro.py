import turtle as turtle
import random

color_list = ['red', 'green', 'blue', 'orange', 'black',
              'yellow', 'brown', 'purple', 'pink', 'gold', 'silver', "gray"]

timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.shape("turtle")
turtle.colormode(255)
timmy_the_turtle.speed('fastest')


for blank in range(45):
    timmy_the_turtle.color(random.choice(color_list))
    timmy_the_turtle.circle(100)
    current_heading = timmy_the_turtle.heading()
    timmy_the_turtle.setheading(current_heading + 10)

screen = turtle.Screen()
screen.exitonclick()
