from turtle import *
from math import *
t = Turtle()

t.begin_fill()
t.setheading(90)
t.penup()
t.forward(15)
t.pendown()
t.right(90)
t.forward(56.6666666667 + 15)
t.right(90)
for i in range(4):
    t.forward(200)
    t.right(90)
t.fillcolor('red')
t.end_fill()

t.penup()
t.home()
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    t.forward(56.6666666667)
    t.left(90)
    t.forward(56.6666666667)
    t.right(90)
    t.forward(56.6666666667)
t.fillcolor('white')
t.end_fill()
    
    










input('')
