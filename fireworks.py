import turtle
import random
import math
import time

# ---------------- SCREEN SETUP ----------------

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Fireworks Animation")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

colors = [
    "red",
    "yellow",
    "orange",
    "cyan",
    "magenta",
    "lime",
    "white",
    "violet"
]

# ---------------- ROCKET ----------------

def launch_firework(x, target_y):
    y = -320

    while y < target_y:
        pen.clear()

        # rocket
        pen.penup()
        pen.goto(x, y)
        pen.dot(8, "white")

        # small trail
        pen.goto(x, y - 15)
        pen.dot(5, "orange")

        pen.goto(x, y - 28)
        pen.dot(3, "yellow")

        screen.update()
        time.sleep(0.015)

        y += 18

    pen.clear()

# ---------------- EXPLOSION ----------------

def explode(x, y):
    color = random.choice(colors)

    particles = 40

    # create random directions
    directions = []

    for i in range(particles):
        angle = random.uniform(0, 360)
        speed = random.uniform(2, 6)

        directions.append([angle, speed])

    # animation frames
    for frame in range(30):

        pen.clear()

        for angle, speed in directions:

            distance = frame * speed

            new_x = x + math.cos(math.radians(angle)) * distance
            new_y = y + math.sin(math.radians(angle)) * distance

            # gravity effect
            new_y -= frame * frame * 0.15

            pen.penup()
            pen.goto(new_x, new_y)

            size = max(2, 7 - frame // 5)

            pen.dot(size, color)

        screen.update()
        time.sleep(0.025)

    pen.clear()

# ---------------- MAIN LOOP ----------------

for i in range(15):

    x = random.randint(-350, 350)
    y = random.randint(20, 250)

    launch_firework(x, y)
    explode(x, y)

screen.update()

turtle.done()