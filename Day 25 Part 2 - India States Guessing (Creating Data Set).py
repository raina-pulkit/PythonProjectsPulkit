import turtle
import pandas as pd
import os

screen = turtle.Screen()
screen.title("India States guessing game!")
screen.setup(600, 800)
screen.addshape("Political_Map_India.gif")  # First we need to add the image to the screen
# then we can set the image as the turtle shape
turtle.shape("Political_Map_India.gif")

# Now we need to create the Data set of the coordinates of all the states
# First we add the indian states in lexographical order

os.chdir("C:/Users/pulki/PycharmProjects/PythonProjects_Udemy/Intermediate")
indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
                 "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
                 "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
                 "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
                 "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal", "Ladakh", "Jammu & Kashmir",
                 "Puducherry", "Lakshadweep", "Andaman & Nicobar Islands",
                 "Dadra & Nagar Haveli & Daman & Diu", "Chandigarh", "Delhi"]

data = {"Indian_states": indian_states, "x_cor": list(), "y_cor": list()}
# here we created the dictionary that we will convert into a dataframe later

i = len(indian_states)  # this variable will ensure that we add coordinates on a set number of times

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.goto(0, 200)
# this turtle will keep telling us which state to select

font = ("Arial", 10, "italic")

tim.write(indian_states[i-1], font=font)

def onMouseClick(x, y):
    """This function gets the mouse coordinates on click as parameters and then we go ahead and
    set the values of the states coordinates"""

    global i
    data["x_cor"].append(x)
    data["y_cor"].append(y)
    i -= 1

    if i == 0:
        tim.clear()
        df = pd.DataFrame(data)
        df.to_csv("India_States_Coordinates.csv")
        screen.exitonclick()

    tim.clear()
    tim.write(indian_states[i-1], font=font)


turtle.onscreenclick(onMouseClick)
# But we have to click in order of the states that we have added

turtle.mainloop()
'''This is an alternative way of keeping our screen open as we need to 
click on screen and thus we can't #exitonscreen()'''

# screen.exitonclick()
