from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.hideturtle()

        self.update_scoreboard()

    def increase_score(self, score):
        self.score += score
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.update_highscore(self.score)
        self.score = 0
        self.highscore = self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    @staticmethod
    def read_highscore():
        output = None
        with open("./data.txt", "r") as file:
            content = file.read()
            output = int(content)
        return output

    @staticmethod
    def update_highscore(new_highscore):
        with open("./data.txt", "w") as file:
            file.write(str(new_highscore))