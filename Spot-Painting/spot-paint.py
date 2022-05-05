from random import choice
import turtle

colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
          (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

t = turtle.Turtle()
s = turtle.Screen()
s.colormode(255)
t.hideturtle()
t.setheading(225)
t.penup()
t.fd(300)
t.setheading(0)


for j in range(10):
    for i in range(10):
        t.pencolor(choice(colors))
        t.dot(15)
        t.penup()
        t.fd(50)
        t.pendown()
    t.setheading(90)
    t.penup()
    t.fd(50)
    t.setheading(180)
    t.fd(500)
    t.setheading(0)


s.exitonclick()
print(t)
