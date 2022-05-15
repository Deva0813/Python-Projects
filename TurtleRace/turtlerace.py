from random import randint
from turtle import Turtle, Screen

is_race = False
scr = Screen()
scr.setup(width=500, height=400)
userin = scr.textinput("Number", "Enter your color: ")
color = ["red", "orange", "yellow", "purple", "green", "blue"]
y_pos = [-100, -60, -20, 20, 60, 100]
all_t = []

for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color[i])
    t.goto(x=-230, y=y_pos[i])
    all_t.append(t)

if userin:
    is_race = True

while is_race:

    for turtle in all_t:
        if turtle.xcor() > 230:
            is_race = False
            win_t = turtle.pencolor()
            if win_t == userin:
                print(f"You've won! The {win_t} turtle is the winner.")
            else:
                print(f"You've loss! The {win_t} turtle is the winner.")
        dis = randint(0, 10)
        turtle.forward(dis)

scr.exitonclick(
