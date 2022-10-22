from turtle import Turtle, register_shape
register_shape('rocket1.gif')


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("rocket1.gif")
        self.color("white")
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def reset(self):
        self.goto(0, -350)

