import pyx

from pyfeyner2.linedeformer.linedeformer import LineDeformer


def _deform_path(path, amplitude, frequency, mirror, symmetric, extra):
    windings = int(frequency * pyx.unit.tocm(path.arclen()) / pyx.unit.tocm(amplitude))
    windings += extra
    if symmetric and windings % 2 == 0:
        windings -= 1
    sign = 1
    if mirror:
        sign = -1

    # TODO: is this necessary?
    #vispath = self.getVisiblePath()
    #curveradii = vispath.curveradius([i / 10.0 for i in range(0, 11)])
    #mincurveradius = None
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
        mypath1 = _deform_path(path, self.amplitude, self.frequency, False, False, self.extra)
        mypath2 = _deform_path(path, self.amplitude, self.frequency, True, False, self.extra)
        if self.mirror:
            mypath1, mypath2 = mypath2, mypath1
        if not self.is3d:
            return [mypath1, mypath2]

        paths = []
        ass, bs = mypath1.intersect(mypath2)
        params1, params2 = [], []

        parity1 = True
        if self.parity3d == 0:
            parity1 = False
        for a in ass[1:]:  # TODO: better endpoint cut vetoing
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

        parity2 = False
        if self.parity3d == 0:
            parity2 = True
        for b in bs[1:]:  # TODO: better endpoint cut vetoing
            if parity2:
                params2.append(b - self.skip3d)
                params2.append(b + self.skip3d)
            parity2 = not parity2
        pathbits2 = mypath2.split(params2)
        on = True
        for pathbit in pathbits2:
            if on:
                paths.append(pathbit)
            on = not on
        return paths


class SineLine(LineDeformer):
    def __init__(self):
        LineDeformer.__init__(self)

    def deform_path(self, path):
        mypath1 = path
        mypath2 = _deform_path(path, self.amplitude, self.frequency, self.mirror, self.symmetric, self.extra)
        if not self.is3d:
            return [mypath1, mypath2]

        paths = []
        ass, bs = mypath1.intersect(mypath2)
        params1, params2 = [], []

        parity1 = True
        if self.parity3d == 0:
            parity1 = False
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

        parity2 = False
        if self.parity3d == 0:
            parity2 = True
        for b in bs:
            if parity2:
                params2.append(b - self.skip3d)
                params2.append(b + self.skip3d)
            parity2 = not parity2
        pathbits2 = mypath2.split(params2)
        on = True
        for pathbit in pathbits2:
            if on:
                paths.append(pathbit)
            on = not on
        return paths


__all__ = ["Sine", "DoubleSine", "SineLine"]
