from turtle import Screen
from paddle import Paddle
from bullet import Bullet
from scoreboard import Scoreboard
from invader import Invader
from bomb import Bomb
import random
import datetime
import time

START_TIME = datetime.datetime.now()
hit_detect = 20


def bullet_fire():
    bullet.status = "fired"
    p_xcor = paddle.xcor()
    bullet.move(p_xcor)


def timer():
    global START_TIME
    elapsed = datetime.datetime.now() - START_TIME
    elapsed = int(str(elapsed).split(".")[0].split(":")[-1])
    return elapsed


# Setup Game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Space Invaders")
screen.tracer(0)

# Create Game Objects
paddle = Paddle((0, -350))
scoreboard = Scoreboard()
bullet = Bullet((0, -350))
# Create and position the invaders in the game window. Each invader is a turtle.
y = 200
invader_list = []
for row in range(0, 3):
    for x in range(-240, 240, 40):
        invader = Invader(x, y)
        invader_list.append(invader)
    y += 30
number_invaders = len(invader_list)

# Move the paddle with keyboard
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(bullet_fire, "space")

# Start Game
game_is_on = True
bomb_list = []

while game_is_on:
    elapsed_time = timer()
    screen.update()

    if bullet.status == "fired":
        bullet.move(paddle.xcor())

    if elapsed_time % 10 == 0:
        for inv in invader_list:
            inv.invader_down()

    # Generate random bombs and move them downwards
    if elapsed_time % 10 == 0:
        bomb_x = random.randint(-200, 200)
        bomb_y = invader_list[0].ycor()  # y coordinate of the first element in the invader list
        bomb = Bomb((bomb_x, bomb_y))
        time.sleep(0.2)
        bomb_list.append(bomb)

    for bomb in bomb_list:
        bomb.move()

    # Detect Bullet and Invader Hit
    for inv in invader_list:
        if bullet.distance(inv) < hit_detect:
            inv.hideturtle()  # Hide the turtle where the ball hit
            invader_list.remove(inv)  # Remove the turtle from the brick list
            scoreboard.point()
            bullet.reset_bullet(paddle.xcor())

    # Reset bullet if it misses hitting any invader
    if bullet.ycor() == 350:
        bullet.reset_bullet(paddle.xcor())

    # Detect Invader Bomb and Paddle Hit
    for bomb in bomb_list:
        if bomb.distance(paddle) < hit_detect:
            scoreboard.reduce_life()
            paddle.reset()

        if bomb.ycor() == -350:
            bomb.hideturtle()  # Hide the bomb when it reaches the bottom of the window
            bomb_list.remove(bomb)  # Remove the bomb from the bomb list

    # Game on conditions
    # Game over if all invaders are destroyed
    if scoreboard.score == number_invaders:
        game_is_on = False
        scoreboard.won()

    # Game over if invader hits the paddle
    for inv in invader_list:
        if inv.ycor() == -350:
            game_is_on = False
            scoreboard.lost()

    # Game over if all 3 lives are lost
    if scoreboard.life == 0:
        game_is_on = False
        scoreboard.lost()

screen.exitonclick()
