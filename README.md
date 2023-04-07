# Professor Turtle

This module uses turtle graphics to draw polygons, spirals, and shapes that are made from polygons.

## Usage

The algorithms in pturtle can be run with the interactive interpreter.

    % python
    >>> import pturtle
    >>> pturtle.hexagon()
    >>> pturtle.clear()
    >>> pturtle.star()
    >>> pturtle.clear()
    >>> pturtle.spiral()
    >>> pturtle.clear()

The coordinates of the turtle icon can be set, and accessed, using the set_coords and get_coords functions.

    % python
    >>> import pturtle
    >>> pturtle.get_coords()
    (0.0, 0.0)
    >>> pturtle.set_coords(-50, -50)
    >>> pturtle.get_coords()
    (-50, -50)

The turtle icon can be rotated left or right using the left and right functions.

    % python
    >>> import pturtle
    >>> pturtle.pentagon(100, 'left')
    >>> pturtle.pentagon(100, 'right')
    >>> pturtle.left(180)
    >>> pturtle.pentagon(100, 'left')
    >>> pturtle.pentagon(100, 'right')