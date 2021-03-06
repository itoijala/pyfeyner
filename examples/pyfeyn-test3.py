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

## A B-meson colour-suppressed penguin decay diagram
#            _
# in1 ------(_)------() out1a
#             \  ____() out1b
#              \(____
#                    () out2a
# in2 ---------------() out2b
#

from pyfeyner.user import *
import pyx

fd = FeynDiagram()

in1 = Point(1, 7)
loop_in = Vertex(4, 7)
loop_out = Vertex(7, 7)
out1a = Point(11, 7)
out1b = Point(11, 5)
in2 = Point(1, 0)
out2a = Point(11, 2)
out2b = Point(11, 0)
out1c = Vertex(out1b.x() - 2, out1b.y())
out1d = Vertex(out2a.x() - 2, out2a.y())
vtx = Vertex(out1c.midpoint(out1d).x() - 1.5, out1c.midpoint(out1d).y())

fd.add(Fermion(out2b, in2).addArrow().addLabel(r"\APdown"))
fd.add(Fermion(in1, loop_in).addArrow().addLabel(r"\Pbottom"))
fd.add(Fermion(loop_out, out1a).addArrow().addLabel(r"\Pstrange"))
fd.add(Photon(loop_in, loop_out).bend(-1.5).addLabel(r"\PWplus"))
f_loop, = fd.add(Fermion(loop_in, loop_out).bend(+1.5).addArrow() \
         .addLabel(r"\Pup,\,\Pcharm,\,\Ptop"))
fd.add(Photon(f_loop.fracpoint(0.6), vtx).addLabel(r"\Pphoton/\PZ", displace=0.5).bend(0.5))
fd.add(Fermion(out1b, out1c).addArrow(0.8).addLabel(r"\APup"))
fd.add(Fermion(out1c, out1d).arcThru(vtx))
fd.add(Fermion(out1d, out2a).addArrow(0.2).addLabel(r"\Pup"))

fd.add(Ellipse(x=1, y=3.5, xradius=1, yradius=3.5).setFillStyle(pyx.pattern.crosshatched(0.1, 45)))
fd.add(Ellipse(x=11, y=6, xradius=0.6, yradius=1).setFillStyle(pyx.pattern.hatched135))
fd.add(Ellipse(x=11, y=1, xradius=0.6, yradius=1).setFillStyle(pyx.pattern.hatched135))

fd.draw("pyfeyn-test3.pdf")
