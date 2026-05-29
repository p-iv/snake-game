from turtle import Screen
import time

from golden_food import GoldenFood
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
apple = Food(snake)
golden_apple = GoldenFood(screen, snake)
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food
    if snake.head.distance(apple) < 15:
        apple.spawn()
        snake.grow()
        score.increase_score(score = 1)

    #Collision with golden apple
    if golden_apple.is_active and snake.head.distance(golden_apple) < 15:
        golden_apple.hide_food()
        snake.grow()
        snake.grow()
        score.increase_score(score = 5)

    #Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()