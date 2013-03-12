import math

import matplotlib.colors
import pyx

import pyfeyner2.util


def interpolate(p1, p2, fraction):
    return Point(p1.x + fraction * (p2.x - p1.x), p1.y + fraction * (p2.y - p1.y))


def midpoint(p1, p2):
    return interpolate(p1, p2, 0.5)


def distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)


def intercept(p1, p2):
    "Return the y-intercept of the straight line defined by this point and the argument."
    return p1.y - tangent(p1, p2) * p1.x


def tangent(p1, p2):
    "Return the tangent of the straight line defined by this point and the argument."
    if p2.x != p1.x:
        return (p2.y - p1.y) / (p1.x - p2.x)
    else:
        return float(10000)  # An arbitrary large number to replace infinity


def arg(p1, p2):
    """Return the angle between the x-axis and the straight line defined
    by this point and the argument (cf. complex numbers)."""
    arg = None
    if p2.x == p1.x:
        if p2.y > p1.y:
            arg = math.pi / 2.0
        elif p2.y < p1.y:
            arg = 3 * math.pi / 2.0  # this will be reset to 0 if the points are the same

    if p2.y == p1.y:
        if p2.x < p1.x:
            arg = math.pi
        else:
            arg = 0.0

    if p2.x != p1.x and p2.y != p1.y:
        arg = math.atan((p2.y - p1.y) / (p2.x - p1.x))
        if p2.x < p1.x:
            arg += math.pi
        elif p2.y < p1.y:
            arg += 2 * math.pi

    return math.degrees(arg)


class Point(object):
    color = pyfeyner2.util.create_color_property()
    fillcolor = pyfeyner2.util.create_color_property("_fillcolor")
    from pyfeyner2.util import linestyle
    from pyfeyner2.util import linewidth

    def __init__(self, x, y=None, marker=None, color="k", fillcolor="k", linestyle="-", linewidth="normal", size=0.075, rotation=0):
        try:
            x[0]
        except TypeError:
            if y is None:
                raise ValueError()
            self.x = x
            self.y = y
        else:
            self.xy = x
        self.marker = marker
        self.color = color
        self.fillcolor = fillcolor
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.size = size
        self.rotation = rotation

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def xy(self):
        return (self.x, self.y)

    @xy.setter
    def xy(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def render(self, canvas):
        if self.marker is not None:
            path = self.marker.get_path().transformed(pyx.trafo.rotate(self.rotation, *self.xy)
                                                      .scaled(self.size, None, *self.xy)
                                                      .translated(*self.xy))
            fill = [self.fillcolor]
            stroke = [self.color, self.linestyle, self.linewidth]
            canvas.fill(path, fill)
            canvas.stroke(path, stroke)


__all__ = ["interpolate", "midpoint", "distance", "intercept", "tangent", "arg", "Point"]
