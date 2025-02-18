import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,500)
square=turtle.Turtle()
side=4
length=100
angle=360.0/side
for i in range (side):
    square.forward(length)
    square.right(angle)

turtle.done()
