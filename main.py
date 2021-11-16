from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# detect collision with food - random placement of food and once snake collides with food create another piece
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score_board()


# create scoreboard
# snake length grows
# determine when game should end - hit wall or hit itself


screen.exitonclick()
