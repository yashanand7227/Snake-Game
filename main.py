from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('The Snake Game')

is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15:
        scoreboard.update_score()
        food.refresh()
        snake.extend()

    #Detect collision with walls

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on=False
        scoreboard.game_over()

    #detect collision with its tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on=False
            scoreboard.game_over()

screen.exitonclick()