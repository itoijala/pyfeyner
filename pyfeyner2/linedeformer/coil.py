import pyx

from pyfeyner2.linedeformer.linedeformer import LineDeformer


class Coil(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)
        self.angle = 45

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle

    def deform_path_single(self, path):
        windings = int(self.frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(self.amplitude))
        # Get the whole number of windings and make sure that it's odd so we
        # don't get a weird double-back thing
        windings += self.extra
        if windings % 2 == 0:
            windings -= 1
        sign = 1
        if self.mirror:
            sign = -1
        defo = pyx.deformer.cycloid(self.amplitude, windings, curvesperhloop=10,
                                    skipfirst=0.0, skiplast=0.0, turnangle=self.angle, sign=sign)
        return defo.deform(path)

    def deform_path(self, path):
        mypath = self.deform_path_single(path)
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
