import random
import turtle
from turtle import Turtle,Screen
timmy = Turtle()
#timmy.shape("arrow")
# i=4
# while i:
#     timmy.forward(100)
#     timmy.right(90)
#     i-=1


#create dotted line followed by spaces and again normal line

# for _ in range(50):
#     for _ in range(10):
#         timmy.dot()
#         timmy.penup()
#         timmy.forward(10)
#     for _ in range(10):
#         timmy.forward(10)
#     timmy.pendown()
#     for _ in range(10):
#         timmy.forward(10)
#     timmy.penup()
#     for _ in range(10):
#         timmy.forward(10)
#

#move randomly with each time increasing size,changing color,increasing speed

turtle.colormode(255)
# move = [0,90,180,270]
# size=1
# speed = 1
def color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    v = (r,g,b)
    return v
#
# while True:
#     timmy.width(size)
#     timmy.speed(speed)
#     timmy.pencolor(color())
#     x1 = (random.choice(move))
#     timmy.forward(30)
#     timmy.setheading(x1)
#     size+=0.1
#     speed+=1


#creating  a spirograph with diff colour each time
timmy.speed(0)
gapsize=10
for _ in range(int(360/gapsize)):
    timmy.pencolor(color())
    timmy.circle(100)
    timmy.right(gapsize)




scr = Screen()
scr.exitonclick()