import turtle
s = turtle.Screen()
s.bgcolor('yellow')
t = turtle.Turtle()
s.title('Mano primas kartas')
t.pencolor('green')
t.pensize(5)
t.speed(10) # (0 greiciausias, 1 leciausias, 10 greitas)
laipsniai = 360
kampas = 8
t.fillcolor('purple')
t.begin_fill()
for i in range(kampas):  
    t.lt(laipsniai/kampas)
    t.fd(100)
t.end_fill()
t.end


s.exitonclick()