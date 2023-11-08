import turtle

s = turtle.Screen()
s.bgcolor('yellow')
t = turtle.Turtle()
s.title('Uzduotis')
t.pencolor('green')
t.pensize(5)
t.speed(8) # (0 greiciausias, 1 leciausias, 10 greitas)

colors=('Magenta','LightCoral','LightSkyBlue','LawnGreen','LightBlue','Olive','DeepPink','Green')
x = len(colors) - 3
t.penup()
t.goto(0,-300)
t.pendown()

def figura(i):
    t.pencolor(colors[(i + x) % len(colors)])
    t.fillcolor(colors[i%len(colors)])
    t.begin_fill()

for j in range(15, 2, -1):
    t.pencolor(colors[(j+x)%len(colors)])
    t.fillcolor(colors[j%len(colors)])
    t.begin_fill()
    for i in range(j):
        t.lt(360/j)
        t.fd(100)
    t.end_fill()

s.exitonclick()