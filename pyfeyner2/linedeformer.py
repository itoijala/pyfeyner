import pyx


class LineDeformer(object):
    def __init__(self, is3d=None):
        if not is3d is None:
            self.is3d = is3d

    @property
    def is3d(self):
        return self._is3d

    @is3d.setter
    def is3d(self, is3d):
        self._is3d = is3d

    def deform_path_single(self, path):
        """Deform the given path to a single path."""
        pass

    def deform_path(self, path):
        """Deform the given path to a sequence of paths."""
        pass


class Straight(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self, is3d=False)

    def deform_path_single(self, path):
        return path

    def deform_path(self, path):
        return [path]

class Sine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self, is3d=False)
        self.arcradius = 0.25
        self.frequency = 1.0
        self.extrahalfs = 0
        self.inverted = False

    def deform_path_single(self, path):
        windings = int(self.frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(self.arcradius))
        windings += self.extrahalfs
        sign = 1
        if self.inverted:
            sign = -1
        defo = pyx.deformer.cycloid(self.arcradius, windings, curvesperhloop=5,
                                    skipfirst=0.0, skiplast=0.0, turnangle=0, sign=sign)
        return defo.deform(path)

    def deform_path(self, path):
        return [self.deform_path_single(path)]

class Cycloid(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self, is3d=False)
        self.arcradius = 0.25
        self.frequency = 1.3
        self.extras = 0
        self.inverted = False
        self.skipsize3d = 0.04
        self.parity3d = 0

    def deform_path_single(self, path):
        windings = int(self.frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(self.arcradius))
        # Get the whole number of windings and make sure that it's odd so we
        # don't get a weird double-back thing
        windings += 2 * self.extras
        if windings % 2 == 0:
            windings -= 1
        sign = 1
        if self.inverted:
            sign = -1
        defo = pyx.deformer.cycloid(self.arcradius, windings, curvesperhloop=10,
                                    skipfirst=0.0, skiplast=0.0, sign=sign)
        return defo.deform(path)

    def deform_path(self, path):
        mypath = self.deform_path_single(path)
        if not self.is3d:
            return [mypath]
        para = pyx.deformer.parallel(0.001)
        ass, bs, cs = para.normpath_selfintersections(mypath.normpath(), epsilon=0.01)
        coil_params = []
        for b in bs:
            coil_params.append(b[self.parity3d] - self.skipsize3d)
            coil_params.append(b[self.parity3d] + self.skipsize3d)
        pathbits = mypath.split(coil_params)
        on = True
        paths = []
        for pathbit in pathbits:
            if on:
                paths.append(pathbit)
            on = not on
        return paths

def standard_deformer(name):
    return standard_deformer.table.get(name, None)()

standard_deformer.table = {"straight" : Straight,
                           "sine" : Sine,
                           "cycloid" : Cycloid}
