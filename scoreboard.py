from turtle import Turtle

STARTING_SCORE = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.current_score = STARTING_SCORE
        self.write(
            arg=f"Score: {self.current_score}",
            move=False,
            align="center",
            font=("Arial", 23, "normal")
        )

    def update_score_board(self):
        self.clear()
        self.current_score += 1
        self.write(
            arg=f"Score: {self.current_score}",
            move=False,
            align="center",
            font=("Arial", 23, "normal")
        )
