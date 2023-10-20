from turtle import Turtle, Screen
import random

screen = Screen()
xpos = int(screen.textinput("Dimension X", "What's your x dimension of screen: "))
ypos = int(screen.textinput("Dimension Y", "What's your y dimension of screen: "))
screen.setup(xpos, ypos)

color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

raceOn = False

user_bet = screen.textinput("Your Bet", "Which turtle wins? Enter your color: ")
l = []
for i in range(6):
    c = random.choice(color)
    color.remove(c)
    t = Turtle("turtle")
    t.speed("fastest")
    t.color(c)
    t.penup()
    t.goto(-xpos // 2 + 20, i * (ypos // 7) - (ypos // 7) * 2 - ypos // 14)
    l.append(t)

if user_bet:
    raceOn = True

while raceOn:
    for i in l:
        if i.xcor() > (xpos // 2 - 20):
            raceOn = False
            print(i.pencolor().title(), " won!")
            if user_bet == i.pencolor():
                print("You bet rightly!")
            else:
                print("Oops... wrong guess...")
        i.forward(random.randint(0, 10))
screen.exitonclick()
