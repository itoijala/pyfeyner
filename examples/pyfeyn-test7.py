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
from pyx import *

fd = FeynDiagram()

in1 = Point(-4,  2)
in2 = Point(-4, -2)
out1 = Point(4, -2)
out2 = Point(4,  2)
in_vtx = Vertex(-2, 0, mark=CircleMark())
out_vtx = Vertex(2, 0, mark=CircleMark())

fa1 = Fermion(in1, in_vtx).addArrow().addLabel(r"\Pelectron")
fa2 = Fermion(in_vtx, in2).addArrow().addLabel(r"\Ppositron")
bos = Photon(in_vtx, out_vtx).addLabel(r"\Pphoton/\PZ")
fb1 = Fermion(out1, out_vtx).addArrow(0.2).addLabel(r"\APquark")
fb2 = Fermion(out_vtx, out2).addArrow(0.8).addLabel(r"\Pquark")
glu = Gluon(midpoint(out_vtx, out1), midpoint(out_vtx, out2))
glu.invert().bend(0.5).addLabel("\Pgluon", displace=0.25)

numcopies = 10
angle = 0.8
c1 = fd.drawToCanvas()
c2 = canvas.canvas()
c2.insert(c1, [trafo.rotate(-numcopies*angle)])

c = canvas.canvas()
for i in range(numcopies):
    trans = 1 - ((i+1)/float(numcopies))**8
    c.insert(c2, [trafo.rotate((i+1)*angle), color.transparency(trans)])
    c.insert(c1, [trafo.translate(0.1 - 0.01*(i+1), -5 + 0.05*(i+1)), color.transparency(trans)])

c.writetofile("pyfeyn-test7.pdf")
