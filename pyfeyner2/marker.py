import math

import pyx


class Circle(object):
    def __init__(self):
        pass

    def get_path(self):
        return pyx.path.circle(0, 0, 1).path()


class Polygon(object):
    def __init__(self, corners=3):
        self.corners = corners

    @property
    def corners(self):
        return self._corners

    @corners.setter
    def corners(self, corners):
        self._corners = corners

    def get_path(self):
        return pyx.box.polygon([(- math.sin(i * 2 * math.pi / self.corners),
                                 + math.cos(i * 2 * math.pi / self.corners))
                  for i in range(self.corners)]).path()


class Star(object):
    def __init__(self, rays=3, raysize=0.67):
        self.rays = rays
        self.raysize = raysize

    @property
    def rays(self):
        return self._rays

    @rays.setter
    def rays(self, rays):
        self._rays = rays

    @property
    def raysize(self):
        return self._raysize

    @raysize.setter
    def raysize(self, raysize):
        self._raysize = raysize

    def get_path(self):
        return pyx.box.polygon([(- (1 - self.raysize * (i % 2)) * math.sin(i * math.pi / self.rays),
                                 + (1 - self.raysize * (i % 2)) * math.cos(i * math.pi / self.rays))
                  for i in range(2 * self.rays)]).path()


__all__ = ["Circle", "Polygon", "Star"]
