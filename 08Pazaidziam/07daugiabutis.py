import turtle
s = turtle.Screen()
s.bgcolor('black')
t = turtle.Turtle()
s.title('Uzduotis')
t.pencolor('red')
t.pensize(2)
t.speed(5)

t.penup()
t.goto(-380,250)
t.pendown()

for i in range(6):
    t.fd(30)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(100)
    t.backward(90)
    t.lt(90)
    t.fd(30)
    t.backward(15)
    t.right(90)
    t.fd(90)
    t.lt(90)
    t.backward(15)
    t.penup()
    t.fd(100)
    t.pendown()







s.exitonclick()