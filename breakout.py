import turtle

# Set up the screen
win = turtle.Screen()
win.title("Breakout")
win.bgcolor("black")
win.setup(width=800, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Brick
bricks = []

for i in range(6):
    for j in range(10):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("blue")
        brick.penup()
        brick.goto(-290 + j*60, 250 - i*30)
        bricks.append(brick)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
        paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
        paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Paddle collision
    if (ball.dy < 0) and (-240 < ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.color("green")
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if abs(brick.xcor() - ball.xcor()) < 20 and abs(brick.ycor() - ball.ycor()) < 20:
            ball.dy *= -1
            bricks.remove(brick)
            brick.goto(1000, 1000)  # Move the hit brick off the screen

    # Bottom border
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Ball and paddle miss
    if ball.ycor() < -300:
        ball.goto(0, 0)
        ball.dy *= -1

    # Update the screen
    win.update()
