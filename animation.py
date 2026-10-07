import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Behtar Turtle Animation")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.hideturtle()

# Animation loop
n = 36
h = 0

for i in range(360):
    # Dynamic RGB colors using HSV
    color = colorsys.hsv_to_rgb(h, 1, 1)
    r = int(color[0] * 255)
    g = int(color[1] * 255)
    b = int(color[2] * 255)
    
    t.pencolor((r, g, b))
    t.width(i // 100 + 1)
    
    # Pattern drawing logic
    t.forward(i * 1.5)
    t.left(145)
    t.circle(30, 90)
    
    h += 1 / n

turtle.done()