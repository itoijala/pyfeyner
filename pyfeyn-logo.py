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

from pyx import *
c = canvas.canvas()


sep = 0.2


p1 = path.path(
    path.moveto(-3, -4),
    path.lineto(1-sep,0-sep),
    path.moveto(1+sep, 0+sep),
    path.curveto(2,1, 3,1, 4,0),
    path.curveto(5,-1, 6,-1, 7-sep,0-sep),
    path.moveto(7+sep, 0+sep),
    path.curveto(8,1, 9,1, 10,0),
    path.lineto(14,-4)
    )

t1 = path.path(
    path.moveto(14,-4),
    path.lineto(14+sep,-4-sep/2.0),
    path.moveto(14,-4),
    path.lineto(14+sep/2.0,-4-sep)
    )


p2 = path.path(
    path.moveto(14, 4),
    path.lineto(10+sep, 0+sep),
    path.moveto(10-sep, 0-sep),
    path.curveto(9,-1, 8,-1, 7,0),
    path.curveto(6,1, 5,1, 4+sep,0+sep),
    path.moveto(4-sep, 0-sep),
    path.curveto(3,-1, 2,-1, 1,0),
    path.lineto(-3,4)
    )

t2 = path.path(
    path.moveto(-3,4),
    path.lineto(-3-sep,4+sep/2.0),
    path.moveto(-3,4),
    path.lineto(-3-sep/2.0,4+sep)
    )


c.stroke(p1, [color.cmyk.RoyalBlue, style.linewidth.THICK, deco.earrow.LARge, deco.barrow])
c.stroke(t1, [color.cmyk.RoyalBlue, style.linewidth.thick])


c.stroke(p2, [color.cmyk.MidnightBlue, style.linewidth.THICK, deco.earrow.LARge, deco.barrow])
c.stroke(t2, [color.cmyk.MidnightBlue, style.linewidth.thick])


c.writePDFfile("pyfeyn-logo")
