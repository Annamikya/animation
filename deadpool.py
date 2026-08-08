import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Deadpool Animation")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


# Circle helper
def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()

    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


# ---------------- FACE ----------------

# Red face
draw_circle(0, 0, 220, "red")

time.sleep(0.5)

# ---------------- BLACK EYE PATCHES ----------------

pen.color("black")

# Left eye patch
pen.penup()
pen.goto(-70, 100)
pen.setheading(210)
pen.pendown()

pen.begin_fill()

for i in range(2):
    pen.circle(100, 60)
    pen.circle(40, 120)

pen.end_fill()

# Right eye patch
pen.penup()
pen.goto(70, 100)
pen.setheading(-30)
pen.pendown()

pen.begin_fill()

for i in range(2):
    pen.circle(-100, 60)
    pen.circle(-40, 120)

pen.end_fill()

time.sleep(0.5)

# ---------------- WHITE EYES ----------------

# Left eye
pen.penup()
pen.goto(-70, 40)
pen.setheading(70)
pen.pendown()

pen.color("white")
pen.begin_fill()

for i in range(2):
    pen.circle(60, 60)
    pen.circle(20, 120)

pen.end_fill()

# Right eye
pen.penup()
pen.goto(70, 40)
pen.setheading(110)
pen.pendown()

pen.begin_fill()

for i in range(2):
    pen.circle(-60, 60)
    pen.circle(-20, 120)

pen.end_fill()

# ---------------- TEXT ----------------

pen.penup()
pen.goto(-150, -300)
pen.color("red")

pen.write(
    "DEADPOOL",
    font=("Arial", 35, "bold")
)

turtle.done()