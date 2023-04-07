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

The coordinates of the turtle icon can be accessed and modified using the get_coords and set_coords functions.

    % python
    >>> import pturtle
    >>> pturtle.get_coords()
    (0.0, 0.0)
    >>> pturtle.set_coords(-50, -50)
    >>> pturtle.get_coords()
    (-50, -50)

The turtle icon can be rorated a number of degrees using the left function or the right function.

    % python
    >>> import pturtle
    >>> pturtle.pentagon(100, 'left')
    >>> pturtle.pentagon(100, 'right')
    >>> pturtle.left(180)
    >>> pturtle.pentagon(100, 'left')
    >>> pturtle.pentagon(100, 'right')