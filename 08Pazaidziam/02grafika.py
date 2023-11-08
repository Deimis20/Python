import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.color('green')
laipsniai = 360
kampas = 8
for i in range(kampas):  
    t.lt(laipsniai/kampas)
    t.fd(100)

t.circle(60)
t.dot(20)


s.exitonclick()