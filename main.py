from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Boundary
import time

playing = True

while playing:
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    boundary = Boundary()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        scoreboard.print_it()
        screen.update()
        time.sleep(snake.speed)
        snake.move()

        #eating food
        if snake.head.distance(food) < 18:
            food.refresh()
            snake.extend()
            scoreboard.eaten += 1
            if scoreboard.eaten % 10 == 0:
                scoreboard.level += 1
                snake.speed *= 0.68

        #collision with wall
        if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
            # game_is_on = False
            scoreboard.reset()
            snake.destroy()

        #collision with tail
        for segment in snake.snakes[1:]:
            if snake.head.distance(segment) < 10:
                # game_is_on = False
                scoreboard.reset()
                snake.destroy()

screen.exitonclick()