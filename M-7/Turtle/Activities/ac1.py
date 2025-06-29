import turtle

screen = turtle.Screen()
screen.bgcolor("Orange")
screen.setup(width=400, height=300)
screen.title("Welcome to Turtle Window")

pen = turtle.Turtle()

for _ in range(4):
    pen.forward(100)
    pen.left(90)
