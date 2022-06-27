from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.eaten = 0
        self.level = 1
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def print_it(self):
        self.goto(0, 268)
        self.clear()
        self.write(f"Score: {self.eaten}           Level: {self.level}", align="center", font=('Courier', 18, ''))

    def game_over(self):
        self.goto(0, 0)
        #self.clear()
        self.write(f"GAME OVER", align="center", font=('Courier', 18, ''))


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
