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


@property
def linewidth(self):
    return self._linewidth


@linewidth.setter
def linewidth(self, linewidth):
    if linewidth in _linewidth_table:
        linewidth = _linewidth_table[linewidth]
    if not isinstance(linewidth, pyx.style.linewidth):
        linewidth = pyx.style.linewidth(linewidth)
    self._linewidth = linewidth

_linewidth_table = {"THIN" : pyx.style.linewidth.THIN,
                    "THIn" : pyx.style.linewidth.THIn,
                    "THin" : pyx.style.linewidth.THin,
                    "Thin" : pyx.style.linewidth.Thin,
                    "thin" : pyx.style.linewidth.thin,
                    "normal" : pyx.style.linewidth.normal,
                    "thick" : pyx.style.linewidth.thick,
                    "Thick" : pyx.style.linewidth.Thick,
                    "THick" : pyx.style.linewidth.THick,
                    "THIck" : pyx.style.linewidth.THIck,
                    "THICk" : pyx.style.linewidth.THICk,
                    "THICK" : pyx.style.linewidth.THICK}
