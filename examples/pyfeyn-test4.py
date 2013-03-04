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

from pyfeyn.user import *

fd = FeynDiagram()

in1  = Point(-3, 0)
out1 = Point( 3, 0)
vtx1 = Vertex(-1, 0)
vtx2 = Vertex( 1, 0)

higgs1 = Higgs(in1, vtx1).addLabel(r"\PHiggs")
higgs2 = Higgs(vtx2, out1).addLabel(r"\PHiggs")
loop1 = Fermion(vtx1, vtx2).bend(-1).addArrow().addLabel(r"\APtop")
loop1 = Fermion(vtx2, vtx1).bend(-1).addArrow().addLabel(r"\Ptop")

fd.draw("pyfeyn-test4.pdf")
