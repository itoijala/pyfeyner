import math

import pyx

import pyfeyner2._util


class Label(object):
    from pyfeyner2._util import location

    def __init__(self, text, angle=0, location=None):
        self.text = text
        self.angle = angle
        self.location = location

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
        angle -= self.angle
        angle = math.radians(angle)
        w, h = self.width, self.full_height
        r = 2 * max(w, h)
        lc = pyx.path.line(0, 0, r * math.cos(angle), r * math.sin(angle))
        x, y = lc.atend()
        ls = [(1, -2, 1, 2),
              (2, 1, -2, 1),
              (-1, 2, -1, -2),
              (-2, -1, 2, -1)]
        for x1, y1, x2, y2 in ls:
            l = pyx.path.line(x1 * 0.5 * w, y1 * 0.5 * h, x2 * 0.5 * w, y2 * 0.5 * h)
            ps = lc.intersect(l)[1]
            if len(ps) > 0:
                xl, yl = l.at(ps[0])
                if xl * xl + yl * yl < x * x + y * y:
                    x, y = xl, yl
        x, y = pyx.trafo.translate(0.5 * w, 0.5 * h).apply(x, y)
        return pyx.trafo.rotate(self.angle).apply(x, y)

    def render(self, canvas):
        t = pyx.text.defaulttexrunner.text(self.location[0], self.location[1] + self.depth, self.text)
        t.transform(pyx.trafo.rotate(self.angle, *self.location))
        canvas.insert(t)


__all__ = ["Label"]
