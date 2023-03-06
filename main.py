from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

for turt in range(15):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.pu()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.pd()


screen = Screen()
screen.exitonclick()
