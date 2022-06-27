from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randrange(-240, 240, 20)
        rand_y = random.randrange(-240, 240, 20)
        # for any_segment in range(len(snake.snakes) - 1, 0, -1):
        #     x_pos = snake.snakes[any_segment].xcor()
        #     y_pos = snake.snakes[any_segment].ycor()
            #if rand_x in
        self.goto(rand_x, rand_y)