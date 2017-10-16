import turtle 
import random 
    
turtle.setworldcoordinates(0,0,50,50)

tom = turtle.Turtle()
amy = turtle.Turtle()



def setup(turtle1, turtle2):
    turtle1.shape('turtle')
    turtle2.shape('turtle')
    turtle1.up()
    turtle2.up()
    turtle1.color('red')
    turtle2.color('red')
    turtle1.setposition(1, 25)
    turtle2.setposition(1, 25)
    turtle1.down()
    turtle2.down()

    
def newHeading(turtle, angleOfTipsiness):
    turtle1.setheading(random.uniform(-angleOfTipsiness,angleOfTipsiness))
    turtle2.setheading(random.uniform(-angleOfTipsiness,angleOfTipsiness))

def newColors(turtle1, turtle2):
    turtle1x = turtle1.xcor()
    turtle2x = turtle2.xcor()
    if turtle1x > turtle2x:
        turtle1.color('green')
        turtle2.color('red')
    elif turtle2x > turtle1x:
        turtle2.color('green')
        turtle1.color('red')

def tipsyTurtleRace(turtle1, turtle2, angleOfTipsiness, nSteps):
    for i in range(nSteps + 1):
        turtle1.seth(random.uniform(-angleOfTipsiness,angleOfTipsiness))
        turtle2.seth(random.uniform(-angleOfTipsiness,angleOfTipsiness))
        turtle1.forward(1)
        turtle2.forward(1)
        newColors(turtle1, turtle2)











    
    
