from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.type = "apple"
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")

        self.spawn()

    def spawn(self):
        possible_positions = list(range(-260, 261, 20))

        random_x = random.choice(possible_positions)
        random_y = random.choice(possible_positions)

        self.goto(random_x, random_y)