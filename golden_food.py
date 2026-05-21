from food import Food
import random

class GoldenFood(Food):
    def __init__(self, screen):
        self.screen = screen
        self.is_active = False

        super().__init__()

        self.type = "golden_apple"
        self.color("gold")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.hideturtle()

        self.schedule_next_spawn()

    def spawn(self):
        if not self.is_active:
            super().spawn()
            self.showturtle()
            self.is_active = True
            self.screen.ontimer(self.hide_food, 5000)

    def schedule_next_spawn(self):
        random_time = random.randint(20000, 40000)
        self.screen.ontimer(self.spawn, random_time)

    def hide_food(self):
        if self.is_active:
            self.hideturtle()
            self.is_active = False
            self.schedule_next_spawn()