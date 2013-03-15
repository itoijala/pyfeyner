import pyx

from pyfeyner2.deformer.deformer import Deformer
from pyfeyner2.deformer._util import _clean_intersections


def _deform_path(path, amplitude, frequency, mirror, extra, quality, angle):
    windings = int(frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(amplitude))
    # Get the whole number of windings and make sure that it's odd so we
    # don't get a weird double-back thing
    windings += extra
    if windings % 2 == 0:
        windings -= 1
    sign = 1
    if mirror:
        sign = -1

    defo = pyx.deformer.cycloid(amplitude, windings, curvesperhloop=quality,
                                skipfirst=0.0, skiplast=0.0, turnangle=angle, sign=sign)
    return defo.deform(path)


class Coil(Deformer):
    def __init__(self):
        Deformer.__init__(self)
        self.frequency = 1.3
        self.angle = 45

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle

    def deform_path(self, path):
        mypath = _deform_path(path, self.amplitude, self.frequency, self.mirror, self.extra, self.quality, self.angle)
        if not self.is3d:
            return [mypath]

        para = pyx.deformer.parallel(0.001)
        ass, bs, cs = para.normpath_selfintersections(mypath.normpath(), epsilon=0.01)
        coil_params = []
        for b in bs:
            coil_params.append(b[self.parity3d] - self.skip3d)
            coil_params.append(b[self.parity3d] + self.skip3d)
        pathbits = mypath.split(coil_params)
        on = True
        paths = []
        for pathbit in pathbits:
            if on:
                paths.append(pathbit)
            on = not on
        return paths


class CoilLine(Deformer):
    def __init__(self):
        Deformer.__init__(self)
        self.frequency = 1.3
        self.angle = 45

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle

    def deform_path(self, path):
        mypath1 = path
        mypath2 = _deform_path(path, self.amplitude, self.frequency, self.mirror, self.extra, self.quality, self.angle)
        if not self.is3d:
            return [mypath1, mypath2]

        ass, bs = mypath1.intersect(mypath2)
        ass, bs = _clean_intersections([mypath1, mypath2], [ass, bs])
        params1, params2 = [], []
        paths = []

        parity1 = False
        if self.parity3d == 0:
            parity1 = True
        for a in ass:
            if parity1:
                params1.append(a - self.skip3d)
                params1.append(a + self.skip3d)
            parity1 = not parity1
        pathbits1 = mypath1.split(params1)
        on = True
        for pathbit in pathbits1:
            if on:
                paths.append(pathbit)
            on = not on

        parity2 = True
        if self.parity3d == 0:
            parity2 = False

        for b in bs:
            if parity2:
                params2.append(b - self.skip3d)
                params2.append(b + self.skip3d)
            parity2 = not parity2
        para = pyx.deformer.parallel(0.001)
        sas, sbs, scs = para.normpath_selfintersections(mypath2.normpath(), epsilon=0.01)
        coil_params = []
        for b in sbs:
            coil_params.append(b[self.parity3d] - self.skip3d)
            coil_params.append(b[self.parity3d] + self.skip3d)
        params2 += coil_params
        params2.sort()
        pathbits2 = mypath2.split(params2)
        on = True
        for pathbit in pathbits2:
            if on:
                paths.append(pathbit)
            on = not on
        return paths


__all__ = ["Coil", "CoilLine"]
