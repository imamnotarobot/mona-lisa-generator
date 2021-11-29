#Eventualy this will make every art ever

import turtle
import random


t = turtle.Turtle()

t.hideturtle()

t.speed(100)


while True:
  t.color(random.randint(0,256), random.randint(0,256), random.randint(0,256))
  t.forward(1)
  t.left(random.randint(1,360))
