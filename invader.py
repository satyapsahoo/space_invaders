from turtle import Turtle, register_shape
register_shape('invader.gif')


class Invader(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("invader.gif")
        self.penup()
        self.goto(x_pos, y_pos)
        self.y_move = 1

    def invader_down(self):
        new_y = self.ycor() - self.y_move
        xcor = self.xcor()
        self.goto(xcor, new_y)
