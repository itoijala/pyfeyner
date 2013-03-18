import math

import pyx

from pyfeyner2.label import Label
import pyfeyner2._util


class Marker(object):
    from pyfeyner2._util import location
    color = pyfeyner2._util.create_color_property()
    fillcolor = pyfeyner2._util.create_color_property("_fillcolor")
    from pyfeyner2._util import linestyle
    from pyfeyner2._util import linewidth

    def __init__(self, location, color="k", fillcolor="k", linestyle="-", linewidth="normal", size=0.075, rotation=0):
        self.location = location
        self.color = color
        self.fillcolor = fillcolor
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.size = size
        self.rotation = rotation
        self.labels = []

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

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, labels):
        if isinstance(labels, str):
            self.labels = []
            self.add_label(labels)
        else:
            self._labels = labels

    def add_label(self, label, displacement=0.3, angle=0):
        if isinstance(label, str):
            label = Label(label)
        displacement += self.size
        x, y = label.get_bounding_point(angle + 180)
        label.location = pyx.trafo.translate(*pyx.trafo.rotate(angle).apply(displacement, 0)).translated(*self.location).apply(-x, -y)
        self._labels.append(label)

    def render(self, canvas):
        path = self.get_path().transformed(pyx.trafo.rotate(self.rotation)
                                           .scaled(self.size)
                                           .translated(*self.location))
        if self.fillcolor is not None:
            fill = [self.fillcolor]
            canvas.fill(path, fill)
        if self.color is not None:
            stroke = [self.color, self.linestyle, self.linewidth]
            canvas.stroke(path, stroke)
        for label in self.labels:
            label.render(canvas)


class Circle(Marker):
    def __init__(self, location, **kwargs):
        Marker.__init__(self, location, **kwargs)

    def get_path(self):
        return pyx.path.circle(0, 0, 1).path()


class Polygon(Marker):
    def __init__(self, location, corners=3, **kwargs):
        Marker.__init__(self, location, **kwargs)
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


class Star(Marker):
    def __init__(self, location, rays=3, raysize=0.67, **kwargs):
        Marker.__init__(self, location, **kwargs)
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



def standard_marker(name):
    return standard_marker.table.get(name, None)()

standard_marker.table = {"circle" : Circle,
                         "polygon" : Polygon,
                         "star" : Star,
                        }


__all__ = ["Marker", "Circle", "Polygon", "Star"]
