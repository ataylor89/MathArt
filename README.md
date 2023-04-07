# Professor Turtle

This module uses turtle graphics to draw polygons, spirals, and shapes that are made from polygons.

## Usage

The algorithms in this module can be run with the interactive interpreter.

    % python
    >>> import profturtle
    >>> profturtle.hexagon()
    >>> profturtle.clear()
    >>> profturtle.star()
    >>> profturtle.clear()
    >>> profturtle.spiral()
    >>> profturtle.clear()

Coordinates can be set, and retrieved, using the set_coords and get_coords functions.

    % python
    >>> import profturtle
    >>> profturtle.get_coords()
    (0.0, 0.0)
    >>> profturtle.set_coords(-50, -50)
    >>> profturtle.get_coords()
    (-50, -50)

The turtle icon can be rotated using the left function or the right function.

    % python
    >>> import profturtle
    >>> profturtle.pentagon(100, 'left')
    >>> profturtle.pentagon(100, 'right')
    >>> profturtle.left(180)
    >>> profturtle.pentagon(100, 'left')
    >>> profturtle.pentagon(100, 'right')