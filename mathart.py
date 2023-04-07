import turtle

turtle.shape('turtle')

def set_coords(x, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.showturtle()

def get_coords():
    return (turtle.xcor(), turtle.ycor())

def clear():
    turtle.clear()

def rotate(theta):
    turtle.left(theta)

def hexagon(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(6):
            turtle.forward(sidelength)
            turtle.right(60)
    elif direction == 'ccw':
        for i in range(6):
            turtle.forward(sidelength)
            turtle.left(60)

def hexagons(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            hexagon(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            hexagon(sidelength, direction)
            turtle.left(5)

def pentagon(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(72)
    elif direction == 'ccw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(72)

def pentagons(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            pentagons(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            pentagons(sidelength, direction)
            turtle.left(5)

def star(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(144)
    elif direction == 'ccw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(144)

def stars(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            star(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            star(sidelength, direction)
            turtle.left(5)

def square(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif direction == 'ccw':
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)

def squares(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            square(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            square(sidelength, direction)
            turtle.left(5)

def triangle(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(3):
            turtle.forward(sidelength)
            turtle.right(120)
    elif direction == 'ccw':
        for i in range(3):
            turtle.forward(sidelength)
            turtle.left(120)

def triangles(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            triangles(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            triangles(sidelength, direction)
            turtle.left(5)

def spiral(direction='cw'):
    if direction == 'cw':
        for i in range(72):
            triangle(i*5, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            triangle(i*5, direction)
            turtle.left(5)