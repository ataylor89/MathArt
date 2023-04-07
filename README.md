# MathArt

This module uses turtle graphics to draw polygons, circles made from polygons, and spirals.

## Usage

The algorithms in this module can be run inside the interactive Python environment.

    % python
    >>> import mathart
    >>> mathart.draw_pentagon()
    >>> mathart.clear()
    >>> mathart.draw_hexagon()
    >>> mathart.clear()
    >>> mathart.draw_star()
    >>> mathart.clear()

The coordinates of the turtle icon can be set using set_coords and retrieved using get_coords.

    % python
    >>> import mathart
    >>> mathart.get_coords()
    (0.0, 0.0)
    >>> mathart.set_coords(-50, -50)
    >>> mathart.get_coords()
    (-50, -50)