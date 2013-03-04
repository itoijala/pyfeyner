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

splitsize = 0.15
arcradius = 1.0

c = canvas.canvas()

p = path.path( path.moveto(0,0), path.lineto(10,10) )
coil = deformer.cycloid(arcradius, 15, curvesperhloop=10, skipfirst=0.0, skiplast=0.0, sign=+1)
para = deformer.parallel(0.1)
dp = coil.deform(p)

as, bs, cs = para.normpath_selfintersections(dp.normpath(), 0.01)
#print as, "\n"
#print bs, "\n"
#print cs, "\n"

## Get the appropriate split points around each intersection
coil_params = []
for b in bs:
    coil_params.append(b[0] - splitsize)
    coil_params.append(b[0] + splitsize)
pathbits = dp.split(coil_params)

## Draw the underlying line with some transparency
c.stroke(dp, [style.linewidth.THICK, color.cmyk.Violet, color.transparency(0.8)])

on = True
for pathbit in pathbits:
    if on:
        c.stroke(pathbit, [color.rgb.red, style.linewidth.thick])
    #else:
    #    c.stroke(pathbit, [color.rgb.blue])
    on = not on

c.writetofile("test-3dgluon2.pdf")
