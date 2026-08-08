import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flower Animation")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Draw one petal
def petal():
    for i in range(2):
        pen.circle(100, 60)
        pen.left(120)

# Draw flower
colors = ["red", "pink", "orange", "yellow", "purple"]

for i in range(36):
    pen.color(colors[i % len(colors)])

    petal()

    pen.left(10)

    # Small delay makes it look animated
    time.sleep(0.03)

# Flower center
pen.penup()
pen.goto(0, -25)
pen.pendown()

pen.color("yellow")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

turtle.done()