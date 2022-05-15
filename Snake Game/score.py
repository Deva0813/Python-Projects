from turtle import Turtle
FONT = ("Courier", 15, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0.00, 270)
        self.write(f"Score: {self.score}", align=ALIGN,
                   font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0.0, 0.0)
        self.write("GAME OVER...", align=ALIGN,
                   font=FONT)
