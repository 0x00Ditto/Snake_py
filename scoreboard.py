from turtle import Turtle
ALIGNMENT = "Center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("White")
        self.goto(0,270)
        self.score_update()



    def score_update(self):
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
