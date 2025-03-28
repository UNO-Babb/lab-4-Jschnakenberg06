#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle,sides)
for _ in range(sides):
    myTurtle.forward(50)
    myTurtle.right(360 / sides)

def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    if corner == 1:
        myTurtle.goto(0, 50)
    elif corner == 2:
        myTurtle.goto(50, 50)
    elif corner == 3:
        myTurtle.goto(0, 0)
    elif corner == 4:
        myTurtle.goto(50, 0)
    else:
        return

    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)
    myTurtle.end_fill()

def squaresInSquares(myTurtle, num):
    size = 100
    for_in range(num):
    drawSqaure(myTurtle, size)
    myTurtle.penup()
    myTurtle.backward(10)
    myTurtle.right(90)
    myTurtle.forward(10)
    myTurtle.left(90)
    myTurtle.pendown()
    size += 20

def main():
    myTurtle = turtle.Turtle()
    muTurtle.speed(3)
    myTurtle.hideturtle()

drawPolygon(myTurtle, 100)
# drawPolygon(myTurtle, 8)
# drawPolygon(myTurtle, 3)

# fillCorner(myTurtle, 1)
# fillCorner(myTurtle, 2)
# fillCorner(myTurtle, 3)
# fillCorner(myTurtle, 4)

sqauresInSquares(myTurtle, 5)

turtle.done()



main()
