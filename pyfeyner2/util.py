import matplotlib.colors
import pyx


@property
def color(self):
    return self._color


@color.setter
def color(self, color):
    if isinstance(color, str):
        color = matplotlib.colors.colorConverter.to_rgb(color)
    if not isinstance(color, pyx.color.color):
        color = pyx.color.rgb(*color)
    self._color = color


@property
def linestyle(self):
    return self._linestyle


@linestyle.setter
def linestyle(self, linestyle):
    if linestyle in _linestyle_table:
        linestyle = _linestyle_table[linestyle]
    self._linestyle = linestyle

_linestyle_table = {"-" : pyx.style.linestyle.solid,
                    "--" : pyx.style.linestyle.dashed,
                    ":" : pyx.style.linestyle.dotted,
                    "-." : pyx.style.linestyle.dashdotted}
