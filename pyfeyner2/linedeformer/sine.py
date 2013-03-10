import pyx

from pyfeyner2.linedeformer.linedeformer import LineDeformer


class Sine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)

    def deform_path_single(self, path):
        windings = int(self.frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(self.amplitude))
        windings += self.extra
        if self.symmetric and windings % 2 == 0:
            windings -= 1
        sign = 1
        if self.mirror:
            sign = -1
        defo = pyx.deformer.cycloid(self.amplitude, windings, curvesperhloop=10,
                                    skipfirst=0.0, skiplast=0.0, turnangle=0, sign=sign)
        return defo.deform(path)


__all__ = ["Sine"]
