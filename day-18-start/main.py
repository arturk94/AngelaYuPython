import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.color("red")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)

    return (r,g,b)

directions = [0, 90, 180, 270]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def random_walk():
    tim.forward(random.choice([10, 20, 30]))
    tim.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# tim.pensize(15)
tim.speed("fastest")
# for _ in range(500):
#     tim.color(random_color())
#     random_walk()

draw_spirograph(5)





screen = t.Screen()
screen.exitonclick()
