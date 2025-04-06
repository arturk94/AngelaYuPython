from turtle import Turtle as t, Screen as s
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = s()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

# Create and move the paddle
r_paddle = Paddle((350,0))

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")

# Create another paddle
l_paddle = Paddle((-350,0))

screen.onkey(l_paddle.go_up,"z")
screen.onkey(l_paddle.go_down, "s")


# Create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()


# Keep score

game_is_on = True
while game_is_on:
     time.sleep(ball.move_speed)
     screen.update()
     ball.move()

     # Detect collision with wall and bounce
     if ball.ycor() > 280 or ball.ycor() < -280:
          print(ball.ycor())
          ball.bounce_y()

     # Detect collision with paddle
     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
          ball.bounce_x()

     # Detect R paddle misses
     if ball.xcor() > 380:
          ball.reset_position()
          scoreboard.l_point()

     # Detect L paddle misses
     if ball.xcor() < -380:
          ball.reset_position()
          scoreboard.r_point()


screen.exitonclick()