import math

import matplotlib.colors
import pyx


def interpolate(p1, p2, fraction):
    return (p1[0] + fraction * (p2[0] - p1[0]), p1[1] + fraction * (p2[1] - p1[1]))


def midpoint(p1, p2):
    return interpolate(p1, p2, 0.5)


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def intercept(p1, p2):
    "Return the y-intercept of the straight line defined by this point and the argument."
    return p1[1] - tangent(p1, p2) * p1[0]


def tangent(p1, p2):
    "Return the tangent of the straight line defined by this point and the argument."
    if p2[0] != p1[0]:
        return (p2[1] - p1[1]) / (p1[0] - p2[0])
    else:
        return float(10000)  # An arbitrary large number to replace infinity


def arg(p1, p2):
    """Return the angle between the x-axis and the straight line defined
    by this point and the argument (cf. complex numbers)."""
    arg = None
    if p2[0] == p1[0]:
        if p2[1] > p1[1]:
            arg = math.pi / 2.0
        elif p2[1] < p1[1]:
            arg = 3 * math.pi / 2.0  # this will be reset to 0 if the points are the same

    if p2[1] == p1[1]:
        if p2[0] < p1[0]:
            arg = math.pi
        else:
            arg = 0.0

    if p2[0] != p1[0] and p2[1] != p1[1]:
        arg = math.atan((p2[1] - p1[1]) / (p2[0] - p1[0]))
        if p2[0] < p1[0]:
            arg += math.pi
        elif p2[1] < p1[1]:
            arg += 2 * math.pi

    return math.degrees(arg)


__all__ = ["interpolate", "midpoint", "distance", "intercept", "tangent", "arg"]
