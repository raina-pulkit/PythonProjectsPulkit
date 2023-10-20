import colorgram
import turtle
import random

colors = colorgram.extract("hirstpainting.jpg", 50)
l = []
turtle.colormode(255)

for i in colors:
    l.append((i.rgb.r, i.rgb.g, i.rgb.b))  #colors come by frequency of occurrence

tim = turtle.Turtle()
tim.speed("fastest")
tim.up()
tim.setpos(-400, -300)
tim.speed(1000)
tim.down()
for i in range(30):
    for j in range(30):
        tim.dot(20, random.choice(l))   #diameter of 10
        tim.up()
        tim.forward(25)
        tim.down()
# '''we could also do
# tim.color(random.choice(l))
#          tim.begin_fill()
#          tim.circle(15)
#          tim.end_fill()
    #          but here we woudl have to manually change the position of turtle as the circle is drawn tangentially'''
    tim.up()
    tim.left((-1*(-1)**(i%2 - 1))*90)
    tim.forward(25)
    tim.left((-1*(-1)**(i%2 - 1))*90)
    tim.forward(25)
    tim.down()

tim.dot(20)
tim.forward(100)
tim.right(90)
tim.forward(20)
tim.dot(40)





screen = turtle.Screen()
screen.exitonclick()