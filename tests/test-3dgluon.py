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

from pyx import *

splitsize = 0.25
arcradius = 2.0

c = canvas.canvas()

p = path.path( path.moveto(0,0), path.lineto(10,10) )
coil = deformer.cycloid(arcradius, 11, curvesperhloop=10, skipfirst = 0.0, skiplast = 0.0, sign = +1)
para = deformer.parallel(0.415 * arcradius)
dp = coil.deform(p)
pp = para.deform(p)

as, bs = pp.intersect(dp)

on = True
coil_params = []
for b in bs:
    if on:
        coil_params.append(b - splitsize)
        coil_params.append(b + splitsize)
    on = not on

pathbits = dp.split(coil_params)

#c.stroke(dp, [style.linewidth.THICK])
on = True
for pathbit in pathbits:
    if on:
        c.stroke(pathbit, [style.linewidth.THICK])
    on = not on

c.writetofile("test-3dgluon.pdf")
