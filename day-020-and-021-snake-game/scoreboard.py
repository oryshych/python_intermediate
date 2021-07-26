from turtle import Turtle
ALIGMENT = "center"
FONT = "Arial", 22, "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGMENT, font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=(FONT))

    def score_init(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()





    # def score(self):
    #     if snake.head.distance(food) < 15:
    #         score += 1