#!/usr/bin/env python2

#
# PyFeyn - a simple Python interface for making Feynman diagrams.
# Copyright (C) 2007 Andy Buckley
#
# PyFeyn is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PyFeyn is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with PyFeyn; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from pyfeyn.user import *

fd = FeynDiagram()

i1 = Point(-4, +2)
i2 = Point(-4, -2)
v1 = Vertex(-2, 0, mark=CircleMark())
v2 = Vertex(+2, 0, mark=CircleMark())
o1 = Point(+4, +2)
o2 = Point(+4, -2)

l1 = Fermion(i1, v1).addArrow()
l2 = Fermion(v1, i2).addArrow()
l1 = Fermion(o1, v2).addArrow(0.25)
l2 = Fermion(v2, o2).addArrow(0.8)
g1 = Gluino(v1, v2).bend(1.5).set3D()
g2 = Gaugino(v1, v2).bend(-1.5).set3D()
g3 = Graviton(midpoint(v2,o2), midpoint(v2,o1)).bend(0.5).set3D()
g1.setStyles([color.rgb.red])

lab = Label("A silly SUSY / graviton demo", x=0, y=2.2)

fd.draw("pyfeyn-test6.pdf")
