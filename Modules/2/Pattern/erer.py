import turtle
t = turtle.Turtle()
t.speed(1)
t.pensize(2)
t.penup()
t.goto(-100, 0)
t.pendown()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
t.penup()
t.goto(-30, 50)
t.pendown


