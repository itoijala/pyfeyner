import pyx


class Diagram(object):
    def __init__(self):
        self._objects = []

    def add(self, obj):
        self._objects.append(obj)

    def render(self, canvas=None):
        if canvas is None:
            canvas = pyx.canvas.canvas()
        for obj in self._objects:
            obj.render(canvas)
        return canvas

    def save(self, filename):
        self.render().writetofile(filename)


__all__ = ["Diagram"]
