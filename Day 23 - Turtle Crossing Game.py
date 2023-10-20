import time, random
from turtle import Turtle, Screen

xdim, ydim = 1024, 756
screen = Screen()
screen.setup(xdim, ydim)
screen.tracer(0) #switch off the animations
screen.colormode(255)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_DISTANCE = -ydim//2 + 30
        self.MOVE_LENGTH = 10
        self.ENDING_POINT = ydim//2 - 30
        self.shape("turtle")
        self.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.penup()
        self.turtlesize(2,2)
        self.goto(0, self.STARTING_DISTANCE)
        self.setheading(90)

    def move_up(self):
        self.forward(self.MOVE_LENGTH)

    def move_down(self):
        new_y = self.STARTING_DISTANCE if (self.ycor() - self.MOVE_LENGTH) < self.STARTING_DISTANCE else self.ycor() - self.MOVE_LENGTH
        self.goto(0, new_y)

    def next_level(self):
        self.goto(0, self.STARTING_DISTANCE)
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


class Cars:   #we don't extend turtle here, becuase we need to create multiple cars
    def __init__(self):
        self.all_cars = []
        self.MOVE_SPEED = 7


    def create_turtle(self):
        new_car = Turtle("square")
        new_car.shapesize(1,2)
        new_car.penup()
        new_car.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        random_y = random.choice(range(-ydim//2 + 100, ydim//2 - 100, 20))
        new_car.goto(xdim//2, random_y)
        self.all_cars.append(new_car)

    def move_all(self):
        for i in self.all_cars:
            i.backward(self.MOVE_SPEED)

    def next_level(self):
        self.MOVE_SPEED += 2


class Scoreboard(Turtle):
    FONT = ("Arial", 30, "italic")

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-420, 324)
        self.writeon()

    def next_level(self):
        self.level += 1
        self.writeon()

    def writeon(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=self.FONT)

    def game_won(self, cars, player):
        self.clear()
        for i in cars.all_cars:
            i.hideturtle()
            i.clear()
        player.hideturtle()
        player.clear()

        self.goto(0,0)
        self.write("CONGRATS YOU WON!", align = "center", font = self.FONT)

    def game_lost(self, cars, player):
        self.clear()

        self.goto(0, 0)
        self.write("Sorry you lost!", align="center", font=self.FONT)


player = Player()
cars = Cars()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()

while game_is_on:
    time.sleep(0.01)
    screen.update()
    screen.onkeypress(player.move_up,"Up")
    screen.onkeypress(player.move_down, "Down")

    if player.ycor() > player.ENDING_POINT:
        player.next_level()
        scoreboard.next_level()
        cars.next_level()

    if scoreboard.level == 25:
        scoreboard.game_won(cars, player)
        game_is_on = False

    decider = random.randint(0,198)

    if random.randint(1,10) == 1:
        cars.create_turtle()
    cars.move_all()

    for car in cars.all_cars:
        if car.distance(player) < 32:
            game_is_on = False
            scoreboard.game_lost(cars, player)

screen.exitonclick()