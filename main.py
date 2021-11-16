from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

SCREEN_MAX_EDGE = 296
SCREEN_MIN_EDGE = -296

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

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score_board()

    if snake.head.xcor() > SCREEN_MAX_EDGE or snake.head.xcor() < SCREEN_MIN_EDGE or snake.head.ycor() > SCREEN_MAX_EDGE or snake.head.ycor() < SCREEN_MIN_EDGE:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
