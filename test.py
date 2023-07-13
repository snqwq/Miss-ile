import turtle
import time

screen = turtle.Screen()
screen.setup(1000, 750)
screen.bgcolor("black")
screen.title("")

explosion = turtle.Turtle()
explosion.hideturtle()
explosion.speed(0)
explosion.shape("circle")
explosion.color("orange")
explosion.penup()
explosion.goto(0, 0)

time.sleep(5)