from turtle import Turtle, Screen
import random
import colorgram

tommy = Turtle()
screen = Screen()
screen.colormode(255)
tommy.shape("arrow")
tommy.color("red")


colors = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]

for i in range(10):
    currentPos = tommy.pos()
    for j in range(10):
        tommy.dot(15, random.choice(colors))
        tommy.penup()
        tommy.fd(35)
        tommy.pendown()
    tommy.penup()
    tommy.setpos(currentPos[0], currentPos[1]+35)
screen.exitonclick()