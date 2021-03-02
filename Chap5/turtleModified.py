import turtle
import random

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()


# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle, lineLen-5)


# drawSpiral(myTurtle, 100)
# myWin.exitonclick()

import turtle


def tree(branchLen, t):
    angle = random.randint(15, 45)
    branchCut = random.randint(5, 15)
    if branchLen > 5:
        t.pensize(width=branchLen/75*6)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-branchCut, t)
        t.left(angle*2)
        tree(branchLen-branchCut, t)
        t.right(angle)
        if branchLen < 30:
            t.pen(pencolor="orange")
        else:
            t.color("green")
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    # t.up()
    # t.backward(100)
    # t.down()
    t.color("green")
    tree(80, t)
    myWin.exitonclick()


main()
