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

from pyfeyn import *
from pyfeyn.user import *
from pyx import color

fd = FeynDiagram()

out1c = Vertex(9, 5)
out1d = Vertex(9, 2)
vtx = Point(7.5, 3.50)

out1c = Vertex(0, 3)
out1d = Vertex(0, 0)
vtx = Point(1.5, 1.501)

f4 = Fermion(out1c, out1d).arcThru(vtx)

fd.draw("test-bend90b.pdf")
