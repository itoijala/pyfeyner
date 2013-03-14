import pyx

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
            import pyfeyner2.point
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

    @property
    def full_height(self):
        return self.height + self.depth

    def get_bounding_point(self, angle):
        angle %= 360
        if angle < 90:
            x, y = angle * self.width / 90.0, 0
        elif angle < 180:
            x, y = self.width, (angle - 90) * self.full_height / 90.0
        elif angle < 270:
            x, y = (1 - (angle - 180) / 90.0) * self.width, self.full_height
        else:
            x, y = 0, (1 - (angle - 270) / 90.0) * self.full_height
        return pyx.trafo.rotate(self.angle).apply(x, y)

    def render(self, canvas):
        t = pyx.text.defaulttexrunner.text(self.x, self.y + self.depth, self.text)
        t.transform(pyx.trafo.rotate(self.angle, *self.xy))
        canvas.insert(t)


__all__ = ["Label"]
