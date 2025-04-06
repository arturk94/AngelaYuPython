from turtle import Turtle as t

STARTING_POSITIONS_LEFT = [(-200, 0), (-200, -20), (-200, -40)]
STARTING_POSITIONS_RIGHT = [(200, 0), (200, -20), (200, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(t):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)