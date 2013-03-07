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
from math import sin, cos

c = canvas.canvas()
omega  = 5.0
numsegs = 50
mag = 2.0*unit.cm

arclength = 10.0*unit.cm
#print arclength
lenperseg = arclength/float(numsegs)
lengths = [i*lenperseg for i in range(0,numsegs+1)]

gradfactor = lenperseg / 3.0
prevpos = (0.0*unit.cm, 5.0*unit.cm)
prevgrad = (gradfactor, gradfactor * omega * mag / unit.cm)
for l in lengths[1:]:
    start = prevpos
    end = (l, 5.0*unit.cm + mag * sin(omega * l / unit.cm))
    grad1 = prevgrad
    grad2 = (gradfactor,
             gradfactor * omega * mag / unit.cm * cos(omega * l / unit.cm))
    m1 = [start[i] + grad1[i] for i in [0,1]]
    m2 = [end[i]   - grad2[i] for i in [0,1]]
    ###
    s1 = start + end
    line = path.line(*s1)
    #c.stroke(line)
    ###
    s2 = (start[0], start[1], m1[0], m1[1], m2[0], m2[1], end[0], end[1])
    curve = path.curve(*s2)
    c.stroke(curve)
    ###
    c1 = path.circle(m1[0], m1[1], 0.05)
    c2 = path.circle(m2[0], m2[1], 0.05)
    l1 = path.line(start[0], start[1], m1[0], m1[1])
    l2 = path.line(end[0], end[1], m2[0], m2[1])
    #c.fill(c1, [color.rgb.red])
    #c.stroke(c1)
    #c.stroke(c2)
    #c.stroke(l1)
    #c.stroke(l2)
    ###
    prevpos = end
    prevgrad = grad2

c.writePDFfile("defotest2")
