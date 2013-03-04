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

from pyx import *

c = canvas.canvas()

c.stroke(path.path(
    path.moveto(0,0),
    path.arc(0, 3, 3, 270, 90)
    ))
#pt_in = Vertex(0, 0)
#pt_out = Vertex(0, 6)
##pt_out = Vertex(6, 0)
#vtx = Vertex(3, 3)

#f = Fermion(pt_in, pt_out).arcThru(vtx)

c.writetofile("test-bend90c.pdf")
