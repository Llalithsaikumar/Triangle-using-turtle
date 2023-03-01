import turtle
import colorsys
import random, colorsys

t = turtle.Turtle()
t.screen.bgcolor("black")

t.penup()
t.goto(-200, -100)
t.pendown()
t.speed(6)

a = 400
h = 0
n = 100


def triangle():
    global a, n, h
    for i in range(30):
        c = colorsys.hsv_to_rgb(h,1,0.6)
        h = h + (1 / n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a = a - 20


triangle()
triangle()

t.hideturtle()
turtle.done()
