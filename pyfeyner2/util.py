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
