fractallizer
============

Draws fractal shapes.  Change the 'y' value to control level of detail, lower gives more detail while higher gives less.

The simplest drawings can be done by changing the sequence of turtle motion to...

    while True:
        turtle.pendown()
        turtle.forward(x)
        turtle.left(x)
        x += y


More complex drawings can be made by adding more motions to the turtle.
