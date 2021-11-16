from turtle import Turtle

STARTING_SCORE = 0
ALIGN = "center"
MOVE = False
FONT = ("Courier", 23, "normal")
TURTLE_COLOR = "white"
BOARD_LOCATION = (0, 265)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(TURTLE_COLOR)
        self.goto(BOARD_LOCATION)
        self.current_score = STARTING_SCORE
        self.display_score()

    def display_score(self):
        self.write(
            f"Score: {self.current_score}",
            MOVE,
            ALIGN,
            FONT
        )

    def update_score_board(self):
        self.clear()
        self.current_score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAMEOVER.",
            MOVE,
            ALIGN,
            FONT
        )
