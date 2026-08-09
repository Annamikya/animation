import turtle
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Captain America Shield")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


# Circle draw function
def filled_circle(radius, color):

    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    pen.pendown()

    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


# Perfect centered star
def draw_star(cx, cy, outer_radius, inner_radius):

    points = []

    # 10 points = 5 outer + 5 inner
    for i in range(10):

        angle = math.radians(90 + i * 36)

        if i % 2 == 0:
            radius = outer_radius
        else:
            radius = inner_radius

        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)

        points.append((x, y))

    pen.penup()
    pen.goto(points[0])
    pen.pendown()

    pen.color("white")
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(point)

    pen.goto(points[0])

    pen.end_fill()


# ========================
# SHIELD
# ========================

# Outer Red
filled_circle(220, "#C8102E")

# White
filled_circle(175, "white")

# Red
filled_circle(130, "#C8102E")

# Blue center
filled_circle(85, "#0033A0")

# ⭐ EXACT CENTER
draw_star(
    0,      # center X
    0,      # center Y
    65,     # star outer size
    27      # star inner size
)

turtle.done()