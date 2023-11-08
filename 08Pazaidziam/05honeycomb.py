import turtle
s = turtle.Screen()
s.bgcolor('black')
t = turtle.Turtle()
s.title('Uzduotis')
t.pencolor('red')
t.pensize(5)
t.speed(10)
colors=('Red','SkyBlue','Red','Green','Magenta','SkyBlue')
for i in range(6):
    t.fillcolor(colors[i%len(colors)])
    t.begin_fill()
    for c in range(6):
        t.fd(100)
        t.lt(60)
    t.fd(100)
    t.rt(60)
    t.end_fill()
s.exitonclick()