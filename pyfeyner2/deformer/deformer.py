class Deformer(object):
    def __init__(self, amplitude=0.25, frequency=1.0, mirror=False, symmetric=False, extra=0, quality=10, is3d=True, skip3d=0.04, parity3d=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.mirror = mirror
        self.symmetric = symmetric
        self.extra = extra
        self.quality = quality
        self.is3d = is3d
        self.skip3d = skip3d
        self.parity3d = parity3d

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, amplitude):
        self._amplitude = amplitude

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        self._frequency = frequency

    @property
    def mirror(self):
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        self._mirror = mirror

    @property
    def symmetric(self):
        return self._symmetric

    @symmetric.setter
    def symmetric(self, symmetric):
        self._symmetric = symmetric

    # TODO: change name?
    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, extra):
        self._extra = extra

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, quality):
        self._quality = quality

    @property
    def is3d(self):
        return self._is3d

    @is3d.setter
    def is3d(self, is3d):
        self._is3d = is3d

    # TODO: change name?
    @property
    def skip3d(self):
        return self._skip3d

    @skip3d.setter
    def skip3d(self, skip3d):
        self._skip3d = skip3d

    # TODO: change name?
    @property
    def parity3d(self):
        return self._parity3d

    @parity3d.setter
    def parity3d(self, parity3d):
        self._parity3d = parity3d

    def deform_path(self, path):
        """Deform the given path to a sequence of paths."""
        pass


__all__ = ["Deformer"]
