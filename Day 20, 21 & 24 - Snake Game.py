import turtle
from turtle import Turtle, Screen
import time, random

SIZE = 20
XDIM, YDIM = 500, 500
screen = Screen()
screen.setup(XDIM, YDIM)
screen.bgcolor('black')
screen.title("Nokia Snake Game")
screen.tracer(0)  # turns off animation and requires update() func call to refresh screen


class Snake:
    all_turtles = []
    turtle.colormode(255)
    resize_factorx, resize_factory = 0.5, 0.5

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_snakebody((-i * self.resize_factorx * 20, 0), 0)

    def add_snakebody(self, position, heading):
        t = Turtle("turtle")
        t.color('white')
        t.penup()
        t.shapesize(self.resize_factorx, self.resize_factory)  # Reshapes turtle by factor 1/2
        turtle.speed(20)
        t.setposition(position)  # turtlesize() returns the factor by which turtle is reduced
        t.setheading(heading)
        self.all_turtles.append(t)

    def extend_snake(self):
        pos = self.all_turtles[-1].position()
        heading = self.all_turtles[-1].heading()
        self.add_snakebody(pos, heading)

    def move(self):
        # while game_status:
        #     for i in range(3):
        #         all_turtles[i].forward(10)
        #     time.sleep(1)
        #     screen.update()
        # this controls every turtle object's movement individually, but this becomes a problem while moving the snake

        for i in range(len(self.all_turtles) - 1, 0, -1):
            self.all_turtles[i].goto(self.all_turtles[i - 1].position())
        self.all_turtles[0].forward(self.all_turtles[0].turtlesize()[0] * 20)

    def up(self):
        if self.all_turtles[0].heading() != 270:
            self.all_turtles[0].setheading(90)

    def down(self):
        if self.all_turtles[0].heading() != 90:
            self.all_turtles[0].setheading(270)

    def left(self):
        if self.all_turtles[0].heading() != 0:
            self.all_turtles[0].setheading(180)

    def right(self):
        if self.all_turtles[0].heading() != 180:
            self.all_turtles[0].setheading(0)

    def reset(self):
        for i in self.all_turtles:
            i.clear()
            i.goto(1000, 1000)

        self.all_turtles.clear()
        self.create_snake()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        randx = random.randint(-(XDIM // 2) + 20, XDIM // 2 - 20)
        randy = random.randint(-(YDIM // 2) + 20, YDIM // 2 - 20)
        self.goto(randx, randy)


class Scoreboard(Turtle):

    # now we need not do f.close() as we used "with" keyword

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(0, YDIM // 2 - 40)
        self.ht()
        with open("highscore.txt", "r") as f:
            self.high_score = int(f.read())
            # Now we need not close the file as it was done using "with" command
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", XDIM // 20, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", False, "center",
                   ("Arial", XDIM // 22, "italic"))
        self.score = -1
        self.update_scoreboard()
        time.sleep(2)

    # def game_over(self):
    #     self.clear()
    #     self.home()
    #     self.write(f"GAME OVER! FINAL SCORE: {self.score}", False, "center", ("Arial", XDIM//22, "italic"))


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

head = snake.all_turtles[0]
game_status = True
j = -5
while game_status:
    screen.update()
    time.sleep(1.5 ** j)
    snake.move()

    # detect collision with food
    if head.distance(food) < 10:  # distance between the head of the snake and the food
        food.refresh()
        snake.extend_snake()
        scoreboard.update_scoreboard()
        j -= 1

    # detect collision with wall
    if head.xcor() < -(XDIM // 2) + 10 or head.xcor() > (XDIM // 2) - 10 or head.ycor() > (
            YDIM // 2) - 10 or head.ycor() < -(YDIM // 2) + 10:
        scoreboard.reset()
        snake.reset()
        head = snake.all_turtles[0]
        j = -5

    # detect collision with tail
    for i in snake.all_turtles[1:]:
        if head.distance(i) < 5:
            scoreboard.reset()
            snake.reset()
            head = snake.all_turtles[0]
            j = -5

screen.exitonclick()
