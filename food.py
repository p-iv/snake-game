from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.snake = snake

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")

        self.spawn()

    def spawn(self):
        possible_positions = list(range(-260, 261, 20))
        while True:
            random_x = random.choice(possible_positions)
            random_y = random.choice(possible_positions)

            if self.snake.segments is None:
                self.goto(random_x, random_y)
                break

            is_overlapping = False
            for segment in self.snake.segments:
                if segment.distance(random_x, random_y) < 15:
                    is_overlapping = True
                    break

            if not is_overlapping:
                self.goto(random_x, random_y)
                break