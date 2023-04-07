# MathArt

This module uses turtle graphics to draw polygons, circles made from polygons, and spirals.

## Usage

The algorithms in this module can be run inside the interactive Python environment.

    % python
    >>> import mathart
    >>> mathart.hexagon()
    >>> mathart.clear()
    >>> mathart.star()
    >>> mathart.clear()
    >>> mathart.spiral()
    >>> mathart.clear()

The coordinates of the turtle icon can be set and retrieved using the set_coords and get_coords functions.

    % python
    >>> import mathart
    >>> mathart.get_coords()
    (0.0, 0.0)
    >>> mathart.set_coords(-50, -50)
    >>> mathart.get_coords()
    (-50, -50)

The turtle icon can be rotated clockwise or counterclockwise with the rotate function.

    % python
    >>> import mathart
    >>> mathart.pentagon(100, 'cw')
    >>> mathart.pentagon(100, 'ccw')
    >>> mathart.rotate(180)
    >>> mathart.pentagon(100, 'cw')
    >>> mathart.pentagon(100, 'ccw')