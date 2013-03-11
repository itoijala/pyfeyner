import pyx

from pyfeyner2.linedeformer.linedeformer import LineDeformer
from pyfeyner2.linedeformer._util import _clean_intersections, _deform_two_paths


def _deform_path(path, amplitude, frequency, mirror, symmetric, extra):
    windings = int(frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(amplitude))
    windings += extra
    if symmetric and windings % 2 == 0:
        windings -= 1
    sign = 1
    if mirror:
        sign = -1

    # TODO: is this necessary?
    ## Get list of curvature radii in the visible path
    #vispath = self.getVisiblePath()
    #curveradii = vispath.curveradius([i / 10.0 for i in range(0, 11)])
    #mincurveradius = None

    ## Find the maximum curvature (set None if straight line)
    #for curveradius in curveradii:
    #    try:
    #        curveradius = abs(mincurveradius / pyx.unit.m)
    #        if (mincurveradius is None or curveradius < mincurveradius):
    #            mincurveradius = curveradius
    #    except:
    #        pass

    ## Use curvature info to increase number of curve sections
    #numhloopcurves = 5
    #if mincurveradius is not None:
    #    numhloopcurves += int(0.1 / mincurveradius)
    numhloopcurves = 10

    defo = pyx.deformer.cycloid(amplitude, windings, curvesperhloop=numhloopcurves,
                                skipfirst=0.0, skiplast=0.0, turnangle=0, sign=sign)
    return defo.deform(path)


class Sine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)

    def deform_path(self, path):
        return [_deform_path(path, self.amplitude, self.frequency, self.mirror, self.symmetric, self.extra)]


class DoubleSine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)
        self.frequency = 0.6

    def deform_path(self, path):
        return _deform_two_paths([_deform_path(path, self.amplitude, self.frequency, False, False, self.extra),
                                  _deform_path(path, self.amplitude, self.frequency, True, False, self.extra)],
                                  self.mirror, self.is3d, self.skip3d, self.parity3d)


class SineLine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)

    def deform_path(self, path):
        return _deform_two_paths([path, _deform_path(path, self.amplitude, self.frequency, self.mirror, self.symmetric, self.extra)],
                                 False, self.is3d, self.skip3d, self.parity3d)


class DoubleSineLine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)
        self.frequency = 0.6

    def deform_path(self, path):
        paths = [path,
                  _deform_path(path, self.amplitude, self.frequency, False, False, self.extra),
                  _deform_path(path, self.amplitude, self.frequency, True, False, self.extra)]
        if self.mirror:
            paths = paths[::-1]
        if not self.is3d:
            return paths

        ass, bs = paths[0].intersect(paths[1])
        ass, cs = paths[0].intersect(paths[2])
        path_intersections = _clean_intersections(paths, [ass, bs, cs])

        output = []
        for i, (path, intersections) in enumerate(zip(paths, path_intersections)):
            params = []
            for j, intersection in enumerate(intersections):
                if j % 3 != i:
                    params.append(intersection - self.skip3d)
                    params.append(intersection + self.skip3d)
            pathbits = path.split(params)
            on = True
            for pathbit in pathbits:
                if on:
                    output.append(pathbit)
                on = not on
        return output


__all__ = ["Sine", "DoubleSine", "SineLine", "DoubleSineLine"]
