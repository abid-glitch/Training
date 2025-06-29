import turtle

screen = turtle.Screen()
screen.bgcolor("Orange")
pen = turtle.Turtle()

pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(50)

pen.pendown()
pen.right(90)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)

turtle.done()
