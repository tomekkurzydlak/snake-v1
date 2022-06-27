from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SPEED_LVL = 0.25
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        self.speed = SPEED_LVL
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        self.snakes.append(new_snake)
        new_snake.setpos(position)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake_nr in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_nr - 1].xcor()
            new_y = self.snakes[snake_nr - 1].ycor()
            self.snakes[snake_nr].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    # def destroy(self):
    #     self.snakes = []
