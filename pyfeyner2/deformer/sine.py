import pyx

from pyfeyner2.deformer.deformer import Deformer
from pyfeyner2.deformer._util import _clean_intersections, _deform_two_paths, _cut_two_paths


def _deform_path(path, amplitude, frequency, mirror, symmetric, extra, quality):
    windings = int(frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(amplitude))
    windings += extra
    if symmetric and windings % 2 == 0:
        windings -= 1
    sign = 1
    if mirror:
        sign = -1

    defo = pyx.deformer.cycloid(amplitude, windings, curvesperhloop=quality,
                                skipfirst=0.0, skiplast=0.0, turnangle=0, sign=sign)
    return defo.deform(path)


class Sine(Deformer):
    def __init__(self):
        Deformer.__init__(self)

    def deform_path(self, path):
        return [_deform_path(path, self.amplitude, self.frequency, self.mirror, self.symmetric, self.extra, self.quality)]


class DoubleSine(Deformer):
    def __init__(self):
        Deformer.__init__(self)
        self.frequency = 0.6

    def deform_path(self, path):
        return _deform_two_paths([_deform_path(path, self.amplitude, self.frequency, False, False, self.extra, self.quality),
                                  _deform_path(path, self.amplitude, self.frequency, True, False, self.extra, self.quality)],
                                  self.mirror, self.is3d, self.skip3d, self.parity3d)


class SineLine(Deformer):
    def __init__(self):
        Deformer.__init__(self)

    def deform_path(self, path):
        return _deform_two_paths([path, _deform_path(path, self.amplitude, self.frequency, self.mirror, self.symmetric, self.extra, self.quality)],
                                 False, self.is3d, self.skip3d, self.parity3d)


class DoubleSineLine(Deformer):
    def __init__(self):
        Deformer.__init__(self)
        self.frequency = 0.6

    def deform_path(self, path):
        paths = [path,
                  _deform_path(path, self.amplitude, self.frequency, False, False, self.extra, self.quality),
                  _deform_path(path, self.amplitude, self.frequency, True, False, self.extra, self.quality)]
        if not self.is3d:
            return paths

        ass, bs = paths[0].intersect(paths[1])
        ass, cs = paths[0].intersect(paths[2])
        path_intersections = _clean_intersections(paths, [ass, bs, cs])
        output = []

        params = []
        for intersection in path_intersections[0]:
                params.append(intersection - self.skip3d)
                params.append(intersection + self.skip3d)
        pathbits = paths[0].split(params)
        on = True
        for pathbit in pathbits:
            if on:
                output.append(pathbit)
            on = not on

        return output + _cut_two_paths(paths[1:], path_intersections[1:], self.skip3d, self.parity3d)


__all__ = ["Sine", "DoubleSine", "SineLine", "DoubleSineLine"]
