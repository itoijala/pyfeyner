#!/usr/bin/env python2

from pyfeyn.user import *

processOptions()
fd = FeynDiagram()
p1 = Point(-4,  2)
p2 = Point(-4, -2)
g = Gluino(p1, p2)
fd.draw("gluino.pdf")
