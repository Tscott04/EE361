import turtle
t = turtle.Turtle()


def drawPolygon(t, sidelength, numsides):
    turnAngle = 360 / numsides
    for i in range(numsides):
        t.forward(sidelength)
        t.right(turnAngle)

def main():

    t.penup()
    t.goto(-40,40)
    t.pendown()
    drawPolygon(t, 80, 4)
    t.penup()
    t.goto(-25,25)
    t.pendown()
    drawPolygon(t, 50, 4)
    t.penup()
    t.goto(-15,10)
    t.pendown()
    drawPolygon(t, 30, 3)

main()
