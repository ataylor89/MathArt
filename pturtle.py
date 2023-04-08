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

def left(theta):
    turtle.left(theta)

def right(theta):
    turtle.right(theta)

def forward(distance):
    turtle.forward(distance)

def backward(distance):
    turtle.backward(distance)

def triangle(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(3):
            turtle.forward(sidelength)
            turtle.left(120)
    elif direction == 'right':
        for i in range(3):
            turtle.forward(sidelength)
            turtle.right(120)

def triangle360(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(72):
            triangle(sidelength, direction)
            turtle.left(5)
    elif direction == 'right':
        for i in range(72):
            triangle(sidelength, direction)
            turtle.right(5)

def square(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
    elif direction == 'right':
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)

def square360(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(72):
            square(sidelength, direction)
            turtle.left(5)    
    elif direction == 'right':
        for i in range(72):
            square(sidelength, direction)
            turtle.right(5)

def pentagon(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(72)
    elif direction == 'right':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(72)

def pentagon360(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(72):
            pentagon(sidelength, direction)
            turtle.left(5)
    elif direction == 'right':
        for i in range(72):
            pentagon(sidelength, direction)
            turtle.right(5)

def hexagon(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(6):
            turtle.forward(sidelength)
            turtle.left(60)
    elif direction == 'right':
        for i in range(6):
            turtle.forward(sidelength)
            turtle.right(60)

def hexagon360(sidelength=100, direction='left'):
    if direction == 'left':
        for i in range(72):
            hexagon(sidelength, direction)
            turtle.left(5)
    elif direction == 'right':
        for i in range(72):
            hexagon(sidelength, direction)
            turtle.right(5)

def star(sidelength=100, direction='right'):
    if direction == 'left':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(144)
    elif direction == 'right':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(144)

def star360(sidelength=100, direction='right'):
    if direction == 'left':
        for i in range(72):
            star(sidelength, direction)
            turtle.left(5)
    elif direction == 'right':
        for i in range(72):
            star(sidelength, direction)
            turtle.right(5)

def spiral(direction='left'):
    if direction == 'left':
        for i in range(72):
            triangle(i*5, direction)
            turtle.left(5)    
    elif direction == 'right':
        for i in range(72):
            triangle(i*5, direction)
            turtle.right(5)

def angle_of_regular_ngon(n):
    return 180 * (n - 2) / n