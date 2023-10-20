from turtle import Screen, Turtle
import time, random

screen = Screen()
screen.bgcolor("black")
xdim, ydim = 800, 600
screen.setup(xdim, ydim)

screen.title("Ping-Pong")
screen.tracer(0) #Turns off animations thereby requiring us to udpate screen continously

class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(xpos, ypos)

    def go_up(self):
        new_y = self.ycor() + 20 if self.ycor()+20 <= ydim//2 - 40 else ydim//2 - 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20 if self.ycor() - 20 >= -ydim//2 + 40 else -ydim//2 + 40
        self.goto(self.xcor(), new_y)

    def resetPos(self, xdim, ydim):
        self.goto(xdim, ydim)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.xincr = 2
        self.yincr = 2

    def move(self):
        new_x = ball.xcor() + self.xincr
        new_y = ball.ycor() + self.yincr
        self.goto(new_x, new_y)

    def bounce(self):
        self.yincr *= -1

    def hit(self):
        self.xincr *= -1

    def resetPos(self):
        self.goto(0,0)
        self.hit()
        self.bounce()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle() #cause we need only text to appear
        self.lscore, self.rscore = 0, 0
        self.updateBoard()

    def updateBoard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.lscore, align="center", font=("Courier", 80, "italic"))
        self.goto(100, 180)
        self.write(self.rscore, align="center", font=("Courier", 80, "italic"))


paddle1 = Paddle(xdim//2 - 25, 0)
paddle2 = Paddle(-xdim//2 + 25, 0)
ball = Ball()
scoreboard = Scoreboard()


game_is_on = True

screen.listen()
screen.onkey(paddle1.go_up, "Up")               #To get multiple motion in one key press, use onkeypress()
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

while game_is_on:
    time.sleep(0.01)
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    if (ball.xcor() > 345 and ball.distance(paddle1) < 70)   or (ball.xcor() < -345 and ball.distance(paddle2) < 70):
        ball.hit()

    if ball.xcor() > 380 :
        scoreboard.lscore += 1
        scoreboard.updateBoard()
        ball.resetPos()
        paddle1.resetPos(xdim//2 - 25, 0)
        paddle2.resetPos(-xdim // 2 + 25, 0)

    if ball.xcor() < -380:
        scoreboard.rscore += 1
        scoreboard.updateBoard()
        ball.resetPos()
        paddle1.resetPos(xdim // 2 - 25, 0)
        paddle2.resetPos(-xdim // 2 + 25, 0)

    if scoreboard.lscore == 2:
        scoreboard.goto(0,0)
        scoreboard.clear()
        ball.clear()
        paddle1.clear()
        paddle2.clear()
        scoreboard.write("Game Over! Left Wins!!!", align = "center", font = ("Arial", 50, "bold"))
        game_is_on = False

    if scoreboard.rscore == 2:
        scoreboard.goto(0, 0)
        scoreboard.clear()
        scoreboard.write("Game Over! Right Wins!!!", align = "center", font = ("Arial", 50, "bold"))
        game_is_on = False
        ball.hideturtle()
        paddle1.hideturtle()
        paddle2.hideturtle()

    screen.update() #cause animations are disabled

screen.exitonclick()

