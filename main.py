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
apple = Food()
golden_apple = GoldenFood(screen)
score = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food
    if snake.head.distance(apple) < 15:
        for segment in snake.segments:
            if apple.xcor() != segment.xcor() and apple.ycor() != segment.ycor():
                apple.spawn()
        snake.grow()
        score.increase_score(score = 1)

    #Collision with golden apple
    if golden_apple.is_active and snake.head.distance(golden_apple) < 15:
        for segment in snake.segments:
            if apple.xcor() != segment.xcor() and apple.ycor() != segment.ycor():
                golden_apple.hide_food()
        snake.grow()
        score.increase_score(score = 5)

    #Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()