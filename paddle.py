from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position, 0)

    def go_up(self):
        ycor = self.ycor()
        xcor = self.xcor()
        self.goto(xcor, ycor + 20)

    def go_down(self):
        ycor = self.ycor()
        xcor = self.xcor()
        self.goto(xcor, ycor - 20)

