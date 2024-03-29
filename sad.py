import turtle
import time

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("light blue")


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(1)

# draw sun
my_turtle.color("yellow")
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.setposition(150, 150)
my_turtle.begin_fill()
my_turtle.pendown()
my_turtle.circle(50)
my_turtle.end_fill()

# draw rays
my_turtle.penup()
my_turtle.goto(150, 140)
my_turtle.pendown()
my_turtle.goto(150, 130)

my_turtle.penup()
my_turtle.goto(150, 260)
my_turtle.pendown()
my_turtle.goto(150, 270)

my_turtle.penup()
my_turtle.goto(210, 200)
my_turtle.pendown()
my_turtle.goto(220, 200)

my_turtle.penup()
my_turtle.goto(90, 200)
my_turtle.pendown()
my_turtle.goto(80, 200)

# I quad
my_turtle.penup()
my_turtle.goto(185+7, 165-7)
my_turtle.pendown()
my_turtle.goto(185+14, 165-14)

# II quad
my_turtle.penup()
my_turtle.goto(185+7, 235+7)
my_turtle.pendown()
my_turtle.goto(185+14, 235+14)

# III quad
my_turtle.penup()
my_turtle.goto(115-7, 235+7)
my_turtle.pendown()
my_turtle.goto(115-14, 235+14)

# IV quad
my_turtle.penup()
my_turtle.goto(115-7, 165-7)
my_turtle.pendown()
my_turtle.goto(115-14, 165-14)

shift = 90
# draw lines
my_turtle.penup()
my_turtle.goto(-190, -180-shift)
my_turtle.color("yellow")
my_turtle.pensize(6)
my_turtle.pendown()
my_turtle.goto(190, -180-shift)

my_turtle.penup()
my_turtle.goto(-160, -150-shift)
my_turtle.color("purple")
my_turtle.pensize(6)
my_turtle.pendown()
my_turtle.goto(160, -150-shift)

my_turtle.penup()
my_turtle.goto(-130, -120-shift)
my_turtle.color("teal")
my_turtle.pensize(6)
my_turtle.pendown()
my_turtle.goto(130, -120-shift)

# draw cake
my_turtle.penup()
my_turtle.goto(-74, -110-shift)
my_turtle.pendown()
my_turtle.color("white")
my_turtle.goto(50, -110-shift)
my_turtle.left(90)
my_turtle.forward(60)
my_turtle.left(90)
my_turtle.forward(125)
my_turtle.left(90)
my_turtle.forward(60)

# draw candles
my_turtle.penup()
my_turtle.goto(-60, -40-shift)
my_turtle.color("aquamarine")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(-60, -20-shift)

my_turtle.penup()
my_turtle.goto(-40, -40-shift)
my_turtle.color("yellow")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(-40, -20-shift)

my_turtle.penup()
my_turtle.goto(-20, -40-shift)
my_turtle.color("green")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(-20, -20-shift)

my_turtle.penup()
my_turtle.goto(0, -40-shift)
my_turtle.color("pink")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(0, -20-shift)

my_turtle.penup()
my_turtle.goto(20, -40-shift)
my_turtle.color("blue")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(20, -20-shift)


# print message
my_turtle.penup()
my_turtle.goto(-300, 70-shift)
my_turtle.color("purple")
my_turtle.pendown()
my_turtle.write(
    "с праздником ульяш)))", move=False,
    font=("Helvetica", 26, "bold"))


# send the turtle to the corner
my_turtle.penup()
my_turtle.goto(-250, 250)
time.sleep(10)