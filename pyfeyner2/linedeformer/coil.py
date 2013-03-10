import pyx

from pyfeyner2.linedeformer.linedeformer import LineDeformer


def _deform_path(path, amplitude, frequency, mirror, extra, angle):
    windings = int(frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(amplitude))
    # Get the whole number of windings and make sure that it's odd so we
    # don't get a weird double-back thing
    windings += extra
    if windings % 2 == 0:
        windings -= 1
    sign = 1
    if mirror:
        sign = -1
    defo = pyx.deformer.cycloid(amplitude, windings, curvesperhloop=10,
                                skipfirst=0.0, skiplast=0.0, turnangle=angle, sign=sign)
    return defo.deform(path)


class Coil(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)
        self.frequency = 1.3
        self.angle = 45

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle

    def deform_path(self, path):
        mypath = _deform_path(path, self.amplitude, self.frequency, self.mirror, self.extra, self.angle)
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


__all__ = ["Coil"]
