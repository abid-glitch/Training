import turtle

pen = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
pen.speed(0)
pen.hideturtle()

shades = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

while True:
    for i in range(200):
        pen.pencolor(shades[i % len(shades)])
        pen.width(i / 100 + 1)
        pen.forward(i)
        pen.left(59)
    pen.right(239)
    for i in range(200, 0, -1):
        pen.pencolor("black")
        pen.width(i / 100 + 7)
        pen.forward(i)
        pen.right(59)
