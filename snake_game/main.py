from turtle import Screen as s, Turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = s()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

scoreboard.update_score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if the head collides with any segment in the tail:
        # trigger the game over sequence
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
