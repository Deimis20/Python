import turtle
s = turtle.Screen()
s.bgcolor('black')
t = turtle.Turtle()
s.title('Uzduotis')
t.pencolor('red')
t.pensize(5)
t.speed(10)
colors=('Lime','Aqua','Red','Orange')
t.penup()
t.goto(-280,0)
t.pendown()
for j in range(5):
    for i in range(4):
        t.pencolor(colors[i%len(colors)])
        t.left(90)
        t.forward(80)
    t.penup()
    t.fd(160)
    t.pendown()
s.exitonclick()