from turtle import Turtle
import random

class Target(Turtle):
    colors = ['green','orange','yellow','pink','purple','gold','gray','brown','white']
    def __init__(self,x,y):
        super().__init__()
        self.white = False
        self.shapesize(1,2.5)
        self.color(random.choice(self.colors))
        self.shape('square')
        self.penup()
        self.goto(x,y)