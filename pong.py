# Welcome to Po's Python Pong Game
# By Po Kealiinohomoku
# Intensive Project 1

import turtle

# Screen setup

win = turtle.Screen()
win.title("Po's Python Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Gameplay objects


# Player 1 Paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Player 2 Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Game Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# Game Ball Physics
ball.dx = 2
ball.dy = 0


# Player Input Functions


# Paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    win.update()

    # Move Ball Code
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Basic Border Checking
    if ball.xcor() > 390:
        ball.dx = ball.dx * -1

    if ball.xcor() < -390:
        ball.dx = ball.dx * -1
