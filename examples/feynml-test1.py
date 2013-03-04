#!/usr/bin/env python2

#
# PyFeyn - a simple Python interface for making Feynman diagrams.
# Copyright (C) 2005-2010 Andy Buckley, Georg von Hippel
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

from pyfeyn import *
from pyfeyn.feynml import *

fd = FeynDiagram()

in1 = Point(-4,  2)
in2 = Point(-4, -2)
in_vtx = Vertex(-2, 0)
out1 = Point(4, -2)
out2 = Point(4,  2)
out_vtx = Vertex(2, 0)
glue1 = out_vtx.midpoint(out1)
glue2 = out_vtx.midpoint(out2)

l1 = Label("Drell-Yan QCD vertex correction", x=0, y=2)
fa1 = Fermion(in1, in_vtx).addArrow().addLabel(r"\Pelectron")
fa2 = Fermion(in_vtx, in2).addArrow().addLabel(r"\Ppositron")
fa2.addParallelArrow(size=0.1, displace=-0.06, sense=-1)
bos = Photon(in_vtx, out_vtx).addLabel(r"\Pphoton/\PZ")
fb1 = Fermion(out1, glue1).addArrow().addLabel(r"\APquark")
fb1.addParallelArrow(size=0.1, displace=-0.06, sense=-1)
fi1 = Fermion(glue1, out_vtx)
fi2 = Fermion(out_vtx, glue2)
fb2 = Fermion(glue2, out2).addArrow().addLabel(r"\Pquark")
glu = Gluon(glue1, glue2)
glu.invert().bend(0.5).addLabel("\Pgluon", displace=0.25)
glu.addParallelArrow(size=0.1, displace=0.2, sense=-1)

fmlwriter = FeynMLWriter("test.xml")
fmlwriter.describe("""A sample diagram showing a QCD correction to the Drell-Yan process.""")
fmlwriter.diagramToXML(fd)
fmlwriter.close()

