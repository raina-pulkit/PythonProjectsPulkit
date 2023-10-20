import turtle
import pandas as pd
import os

screen = turtle.Screen()
screen.title("India States guessing game!")
screen.setup(600, 800)
screen.addshape("Political_Map_India.gif")  # First we need to add the image to the screen
# then we can set the image as the turtle shape
turtle.shape("Political_Map_India.gif")

os.chdir("C:/Users/pulki/PycharmProjects/PythonProjects_Udemy/Intermediate")

states_data = pd.read_csv("India_States_Coordinates.csv")

total = states_data["Indian_states"].count()
states = states_data["Indian_states"].to_list()

i = 0

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()  # we will use this tutle in order to write every state name

tim2 = turtle.Turtle()
tim2.hideturtle()
tim2.penup()  # we will use this turtle to write Incorrect or correct answer on screen

tim2.goto(0, 200)

font = ("Arial", 10, "italic")
while i < total:
    answer = screen.textinput(title=f"{i}/{total} Guessed right", prompt="Guess the next state!").title()
    tim2.clear()

    if answer == "Exit":
        tim.clear()
        print(f"You need to learn {len(states)} states more! They are:")
        print(states)
        break

    if answer in states:
        tim2.write("CORRECT ANSWER!", font=font)
        i += 1
        state = states_data[states_data["Indian_states"] == answer]
        xcor = state.x_cor.item()
        ycor = state.y_cor.item()

        tim.goto(xcor, ycor - 10)
        tim.write(answer)
        states.remove(answer)

    else:
        tim2.write("INCORRECT! TRY AGAIN!", font=font)

tim2.clear()

if ~len(states):
    tim2.write("CONGRATS YOU WON THE GAME!", font=font)
else:
    tim2.write("Great try! But you have to improve", font=font)
screen.exitonclick()
