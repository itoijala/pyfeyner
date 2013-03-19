import pyx

from pyfeyner2.label import Label
import pyfeyner2._util

class Blob(object):
    from pyfeyner2._util import location
    from pyfeyner2._util import size
    from pyfeyner2._util import angle
    color = pyfeyner2._util.create_color_property()
    fillcolor = pyfeyner2._util.create_color_property("_fillcolor")
    from pyfeyner2._util import linestyle
    from pyfeyner2._util import linewidth
    from pyfeyner2._util import labels

    def __init__(self, location, color="k", fillcolor="w", linestyle="-", linewidth="normal", size=0.5, angle=0):
        self.location = location
        self.color = color
        self.fillcolor = fillcolor
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.size = size
        self.angle = angle
        self.labels = []

    def add_label(self, label, displacement=0.3, angle=0):
        if isinstance(label, str):
            label = Label(label)
        displacement += self.size
        x, y = label.get_bounding_point(angle + 180)
        label.location = pyx.trafo.translate(*pyx.trafo.rotate(angle).apply(displacement, 0)).translated(*self.location).apply(-x, -y)
        self._labels.append(label)
        return self

    def render(self, canvas):
        path = self.get_path().transformed(pyx.trafo.rotate(self.angle)
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


class Ellipse(Blob):
    def __init__(self, location, yscale=1, **kwargs):
        Blob.__init__(self, location, **kwargs)
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


def _standard_blob(name):
    return _standard_blob.table.get(name, None)

_standard_blob.table = {
        "ellipse" : Ellipse,
        }


__all__ = ["Blob", "Ellipse"]
