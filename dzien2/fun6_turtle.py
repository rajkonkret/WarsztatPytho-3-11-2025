import turtle

# rysowanie zółwiem
t = turtle.Turtle()
# t.speed(5)
t.speed(-1)  # najwyższa prędkość
t.setheading(90)
t.penup()
t.goto(0, -200)


# t.pendown()


def branch(t, len1):
    if len1 == 0: return
    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    branch(nt, len1 - 1)
    nt.right(40)
    branch(nt, len1 - 1)


branch(t, 7)
window = turtle.Screen()
window.exitonclick()
