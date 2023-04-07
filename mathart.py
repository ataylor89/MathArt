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

def draw_hexagon(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(6):
            turtle.forward(sidelength)
            turtle.right(60)
    elif direction == 'ccw':
        for i in range(6):
            turtle.forward(sidelength)
            turtle.left(60)

def draw_hexagons(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            draw_hexagon(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            draw_hexagon(sidelength, direction)
            turtle.left(5)

def draw_pentagon(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(72)
    elif direction == 'ccw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(72)

def draw_pentagons(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            draw_pentagon(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            draw_pentagon(sidelength, direction)
            turtle.left(5)

def draw_star(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.right(144)
    elif direction == 'ccw':
        for i in range(5):
            turtle.forward(sidelength)
            turtle.left(144)

def draw_stars(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(1, 73):
            draw_star(i*5, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(1, 73):
            draw_star(i*5, direction)
            turtle.left(5)

def draw_square(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif direction == 'ccw':
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)

def draw_squares(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            draw_square(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            draw_square(sidelength, direction)
            turtle.left(5)

def draw_triangle(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(3):
            turtle.forward(sidelength)
            turtle.right(120)
    elif direction == 'ccw':
        for i in range(3):
            turtle.forward(sidelength)
            turtle.left(120)

def draw_triangles(sidelength=100, direction='cw'):
    if direction == 'cw':
        for i in range(72):
            draw_triangle(sidelength, direction)
            turtle.right(5)
    elif direction == 'ccw':
        for i in range(72):
            draw_triangle(sidelength, direction)
            turtle.left(5)