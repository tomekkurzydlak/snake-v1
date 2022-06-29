from turtle import Turtle

FONT = ('Courier', 18, '')

class Scoreboard(Turtle):
    def __init__(self):
        self.eaten = 0
        self.level = 1
        self.high_score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("score.txt") as file:
            self.high_score = int(file.read())

    def print_it(self):
        self.goto(0, 268)
        self.clear()
        self.write(f"Score: {self.eaten}    Level: {self.level}    High score: {self.high_score}", align="center", font=FONT)

    def reset(self):
        if self.eaten > self.high_score:
            self.high_score = self.eaten
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.eaten = 0
        self.level = 1
        self.print_it()

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-250, -250)
        self.pendown()
        self.goto(-250, 250)
        self.goto(250, 250)
        self.goto(250, -250)
        self.goto(-250, -250)
        self.penup()
