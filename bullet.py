from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("grey")
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=0.3)
        self.penup()
        self.y_move = 5
        self.status = "ready"
        self.goto(position)

    def move(self, p_xcor):
        self.showturtle()
        if self.ycor() == -350:
            xcor = p_xcor
        else:
            xcor = self.xcor()
        new_y = self.ycor() + self.y_move
        self.goto(xcor, new_y)

    def reset_bullet(self, p_xcor):
        self.goto(p_xcor, -350)
        self.status = "ready"
        self.hideturtle()
