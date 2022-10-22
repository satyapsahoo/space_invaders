from turtle import Turtle


class Bomb(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=0.3)
        self.penup()
        self.y_move = -1
        self.goto(position)

    def move(self):
        xcor = self.xcor()
        new_y = self.ycor() + self.y_move
        self.goto(xcor, new_y)
