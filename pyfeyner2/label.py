import pyx

import pyfeyner2.point
import pyfeyner2.util


class Label(object):
    from pyfeyner2.util import x, y, xy

    def __init__(self, text, angle=0, x=None, y=None):
        self.text = text
        self.angle = angle
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif x is not None:
            if isinstance(x, pyfeyner2.point.Point):
                self.xy = x.xy
            else:
                self.xy = x

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        t = pyx.text.defaulttexrunner.text(0, 0, self.text)
        self._width = t.width
        self._height = t.height
        self._depth = t.depth

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def depth(self):
        return self._depth

    def render(self, canvas):
        t = pyx.text.defaulttexrunner.text(self.x, self.y, self.text)
        t.transform(pyx.trafo.rotate(self.angle, *self.xy))
        canvas.insert(t)
