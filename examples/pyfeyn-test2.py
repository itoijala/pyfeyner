#!/usr/bin/env python2

#
# pyfeyner - a simple Python interface for making Feynman diagrams.
# Copyright (C) 2005-2010 Andy Buckley, Georg von Hippel
# Copyright (C) 2013 Ismo Toijala
#
# pyfeyner is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# pyfeyner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with pyfeyner; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from pyfeyner.user import *
import pyx

fd = FeynDiagram()

p1 = Point(2, -2)
p2 = Point(-2, 2)
p3 = Vertex(1.25, 1.25, mark=STAR)
p4 = p1.midpoint(p2)
p5 = p4.midpoint(p1)
p6 = p4.midpoint(p2)

c1 = Circle(center=p1, radius=0.5, fill=[pyx.color.rgb.red], points=[p1])
c2 = Circle(center=p2, radius=0.3, fill=[pyx.color.rgb.green], points=[p2])
e1 = Ellipse(center=p4, xradius=0.5, yradius=1.0,
             fill=[pyx.color.cmyk.MidnightBlue], points=[p4])

l0a = Fermion(p1, p4)
l0b = Fermion(p2, p4)
l1 = NamedLine["gluon"](p2, p1).arcThru(x=3, y=0)
l2 = NamedLine["gravitino"](p1, p2).arcThru(x=0, y=-3).set3D(True)
l3 = Gluon(p2, p3)
l4 = Photon(p1, p3)
l5 = Gluon(p5, p6).bend(-p5.distance(p6)/2.0)
l6 = NamedLine["phantom"](p3,p4)
loop1 = Line(p3, p3).arcThru(x=1.75, y=1.75).addArrow(0.55)

l1.addLabel(r"\Pgluon")
l2.addLabel(r"\Pphoton")
l5.addLabel(r"$\Pgluon_1$")

fd.draw("pyfeyn-test2.pdf")
