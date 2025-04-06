import turtle as t
import random as r

# import colorgram
#
# colors = colorgram.extract('image.jpg', 10)
# colors_list = []
# for color in colors:
#     color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
#     colors_list.append(color_tuple)
#
# print(colors_list)

colors_list = [(246, 242, 234), (248, 240, 244), (236, 246, 240), (239, 242, 248), (216, 148, 92), (221, 78, 57), (45, 94, 146), (151, 64, 91), (232, 219, 93), (217, 65, 85)]
t.colormode(255)

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setposition(-200,-200)

for _ in range(10):
    for _ in range (10):
        tim.dot(20,r.choice(colors_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)



screen = t.Screen()
screen.exitonclick()