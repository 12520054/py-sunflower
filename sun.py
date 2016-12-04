# Spiral Phyllotaxis Demo
#
# Example for VSFX 705
# Turtle Sunflowers - Introduce Phyllotactic Pattern
#
# Author: Deborah R. Fowler
#
# March 21, 2013
# Based on original code in C 1989 using Silicon Graphics Workstations and gl
import math
import turtle


def drawPhyllotacticPattern(turtle, t, petalstart, angle=120, size=2, cspread=4):
    """print a pattern of circles using spiral phyllotactic data"""
    # initialize position
    # turtle.pen(outline=1,pencolor="black",fillcolor="orange")
    turtle.color('black')
    turtle.fillcolor("orange")
    phi = angle * (math.pi / 180.0)
    xcenter = 0.0
    ycenter = 0.0

    # for loops iterate in this case from the first value until < 4, so
    for n in range(0, t):
        r = cspread * math.sqrt(n)
        theta = n * phi

        x = r * math.cos(theta) + xcenter
        y = r * math.sin(theta) + ycenter

        # move the turtle to that position and draw
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        # orient the turtle correctly
        turtle.setheading(n * angle)
        if n > petalstart - 1:
            turtle.color("yellow")
            drawPetal(turtle, x, y)
        else:
            turtle.stamp()


def drawPetal(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('black')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.left(140)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.penup()
    turtle.end_fill()  # this is needed to complete the last petal

tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)  # make the turtle go as fast as possible
drawPhyllotacticPattern(tina, 300, 120, 137.508)
tina.penup()
tina.forward(1000)
tina._position = (150, -250)
print(tina._position)
tina._write('Danh Tran', align='left', font=("Arial", 20, "normal"))
turtle.mainloop()
