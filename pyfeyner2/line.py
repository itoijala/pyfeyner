import pyx

from pyfeyner2.deformer import _standard_deformer
from pyfeyner2.label import Label
from pyfeyner2.point import midpoint, distance, arg
import pyfeyner2._util


class Line(object):
    color = pyfeyner2._util.create_color_property()
    from pyfeyner2._util import linestyle
    from pyfeyner2._util import linewidth

    def __init__(self, start, end, arcthru=None, bend=None, color="k", linestyle="-", linewidth="normal", deformer=None):
        self.start = start
        self.end = end
        if arcthru is not None:
            self.arcthru = arcthru
        else:
            self._arcthru = None
        if bend is not None:
            self.bend(bend)
        self.color = color
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.deformer = deformer
        self.labels = []

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

    # TODO: change name
    @property
    def arcthru(self):
        return self._arcthru

    @arcthru.setter
    def arcthru(self, arcthru):
        self._arcthru = arcthru

    @arcthru.deleter
    def arcthru(self):
        self._arcthru = None

    def straighten(self):
        del self.arcthru

    def bend(self, amount):
        """Bend the line to the right by a given distance."""
        s = self.start
        m = midpoint(self.start, self.end)
        nx = (m[1] - s[1]) / abs(distance(s, m))
        ny = (s[0] - m[0]) / abs(distance(s, m))
        vx = m[0] - s[0]
        vy = m[1] - s[1]
        if (vx * ny - vy * nx) > 0:
            nx *= -1
            ny *= -1
        arcpoint = (m[0] + amount * nx, m[1] + amount * ny)
        self.arcthru = arcpoint

    # TODO: change name?
    @property
    def deformer(self):
        return self._deformer

    @deformer.setter
    def deformer(self, deformer):
        if isinstance(deformer, str):
            deformer = _standard_deformer(deformer)()
        self._deformer = deformer

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

    def add_label(self, label, position=0.5, displacement=0.3, left=False, additional_angle=0, start=False, end=False):
        if isinstance(label, str):
            label = Label(label)
        path = self.get_path()
        if start:
            position = 0
        elif end:
            position = 1
        else:
            if left:
                displacement *= -1
            if self.deformer is not None:
                if displacement > 0 or (displacement == 0 and not left):
                    displacement += self.deformer.amplitude
                else:
                    displacement -= self.deformer.amplitude
        posparam = path.begin() + position * path.arclen()
        px, py = path.at(posparam)
        tangent = path.tangent(posparam, displacement)
        if start or end:
            angle = arg(tangent.atbegin(), tangent.atend())
        else:
            normal = tangent.transformed(pyx.trafo.rotate(-90, px, py))
            angle = arg(normal.atbegin(), normal.atend())
        if start:
            angle += 180
        angle += additional_angle
        x, y = label.get_bounding_point(angle + 180)
        t = pyx.trafo.rotate(angle).apply(displacement, 0)
        if not start and not end and left:
            t = pyx.trafo.rotate(180).apply(*t)
        label.location = pyx.trafo.translate(*t).translated(px, py).apply(-x, -y)
        self._labels.append(label)
        return self

    def get_path(self):
        if self.arcthru is None:
            # This is a simple straight line
            return pyx.path.path(pyx.path.moveto(*self.start),
                                 pyx.path.lineto(*self.end))
        elif (self.start == self.end):
            # This is a tadpole-type loop and needs special care;
            # We shall assume that the arcthrupoint is meant to be
            # the antipode of the basepoint
            arc_center = midpoint(self.start, self.arcthru)
            arc_radius = distance(self.start, self.arcthru) / 2.0

            cargs = (arc_center[0], arc_center[1], arc_radius)
            circle = pyx.path.circle(*cargs)
            line = pyx.path.line(self.start[0], self.start[1], arc_center[0], arc_center[1])
            ass, bs = circle.intersect(line)
            subpaths = circle.split(ass[0])
            cpath = subpaths[0]
            return cpath
        else:
            n13, n23 = None, None
            # Work out line gradients
            try:
                n13 = (self.start[1] - self.arcthru[1]) / (self.start[0] - self.arcthru[0])
            except ZeroDivisionError:
                n13 = 1e100

            try:
                n23 = (self.end[1] - self.arcthru[1]) / (self.end[0] - self.arcthru[0])
            except ZeroDivisionError:
                n23 = 1e100

            # If gradients match,
            # then we have a straight line, so bypass the complexity
            if n13 == n23:
                return pyx.path.path(pyx.path.moveto(*self.start),
                                     pyx.path.lineto(*self.end))

            # Otherwise work out conjugate gradients and midpoints
            m13, m23 = None, None
            try:
                m13 = -1.0 / n13
            except ZeroDivisionError:
                m13 = 1e100
            try:
                m23 = -1.0 / n23
            except ZeroDivisionError:
                m23 = 1e100
            mid13 = midpoint(self.start, self.arcthru)
            mid23 = midpoint(self.end, self.arcthru)

            # Line y-intercepts
            c13 = mid13[1] - m13 * mid13[0]
            c23 = mid23[1] - m23 * mid23[0]

            # Find the centre of the arc
            xcenter = - (c23 - c13) / (m23 - m13)
            ycenter = m13 * xcenter + c13
            arc_center = (xcenter, ycenter)

            # Get the angles required for drawing the arc
            arc_radius = distance(arc_center, self.arcthru)
            arc_angle1 = arg(arc_center, self.start)
            arc_angle2 = arg(arc_center, self.end)
            arc_angle3 = arg(arc_center, self.arcthru)
            arc_args = (arc_center[0], arc_center[1], arc_radius, arc_angle1, arc_angle2)

            # Calculate cross product to determine direction of arc
            vec12 = [self.end[0] - self.start[0], self.end[1] - self.start[1], 0.0]
            vec13 = [self.arcthru[0] - self.start[0], self.arcthru[1] - self.start[1], 0.0]
            cross_product_z = vec12[0] * vec13[1] - vec12[1] * vec13[0]

            if cross_product_z < 0:
                return pyx.path.path(pyx.path.moveto(*self.start),
                                     pyx.path.arc(*arc_args))
            else:
                return pyx.path.path(pyx.path.moveto(*self.start),
                                     pyx.path.arcn(*arc_args))

    def render(self, canvas):
        if self.deformer is not None:
            paths = self.deformer.deform_path(self.get_path())
        else:
            paths = [self.get_path()]
        styles = [self.color, self.linestyle, self.linewidth]
        for path in paths:
            canvas.stroke(path, styles)
        for label in self.labels:
            label.render(canvas)


__all__ = ["Line"]
