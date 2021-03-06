import math

import pyx

from pyfeyner2.label import Label
import pyfeyner2._util


class Marker(object):
    from pyfeyner2._util import location
    from pyfeyner2._util import size
    from pyfeyner2._util import angle
    color = pyfeyner2._util.create_color_property()
    fillcolor = pyfeyner2._util.create_color_property("_fillcolor")
    from pyfeyner2._util import linestyle
    from pyfeyner2._util import linewidth
    from pyfeyner2._util import labels

    def __init__(self, location, color="k", fillcolor="k", linestyle="-", linewidth="normal", size=0.075, angle=0):
        self.location = location
        self.color = color
        self.fillcolor = fillcolor
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.size = size
        self.angle = angle
        self.labels = []

    def label(self, label, displacement=0.3, angle=0):
        if isinstance(label, str):
            label = Label(label)
        displacement += self.size
        x, y = label.get_bounding_point(angle + 180)
        label.location = pyx.trafo.translate(*pyx.trafo.rotate(angle).apply(displacement, 0)).translated(*self.location).apply(-x, -y)
        self._labels.append(label)
        return self

    def render(self, canvas):
        path = self.get_path()
        if path is not None:
            path = path.transformed(pyx.trafo.rotate(self.angle)
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


class Dummy(Marker):
    def __init__(self, location, **kwargs):
        Marker.__init__(self, location, **kwargs)

    @property
    def size(self):
        return 0

    @size.setter
    def size(self, size):
        pass

    def get_path(self):
        return None


class Asterisk(Marker):
    def __init__(self, location, rays=3, **kwargs):
        Marker.__init__(self, location, **kwargs)
        self.rays = rays

    @property
    def fillcolor(self):
        return None

    @fillcolor.setter
    def fillcolor(self, fillcolor):
        pass

    @property
    def rays(self):
        return self._rays

    @rays.setter
    def rays(self, rays):
        self._rays = rays

    def get_path(self):
        elements = []
        for i in range(self.rays):
            elements.append(pyx.path.moveto(0, 0))
            elements.append(pyx.path.lineto(- math.sin(i * 2 * math.pi / self.rays),
                                            + math.cos(i * 2 * math.pi / self.rays)))
        return pyx.path.path(*elements)


class Ellipse(Marker):
    def __init__(self, location, yscale=1, **kwargs):
        Marker.__init__(self, location, **kwargs)
        self.yscale = yscale

    @property
    def yscale(self):
        return self._yscale

    @yscale.setter
    def yscale(self, yscale):
        if yscale > 1:
            self.angle += 90
            yscale = 1.0 / yscale
        self._yscale = yscale

    def get_path(self):
        return pyx.path.circle(0, 0, 1).transformed(pyx.trafo.scale(1, self.yscale))


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


def _standard_marker(name):
    return _standard_marker.table.get(name, None)

_standard_marker.table = {
        "dummy" : Dummy,
        "asterisk" : Asterisk,
        "ellipse" : Ellipse,
        "polygon" : Polygon,
        "star" : Star,
        }


__all__ = ["Marker", "Dummy", "Ellipse", "Polygon", "Star"]
