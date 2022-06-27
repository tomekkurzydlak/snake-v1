
from turtle import Turtle

CURSOR_SIZE = 20
FONT_SIZE = 20
FONT = ('Courier', FONT_SIZE, 'bold')



class Button(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Click to resume", align='center', font=FONT)





