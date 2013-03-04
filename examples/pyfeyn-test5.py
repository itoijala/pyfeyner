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

p1 = Point(-2, 0)
p2 = Point( 2, 0)
fa1 = MultiLine(p1, p2).bend(0.5).addArrow()
c1 = Circle(center=p1, radius=0.5, fill=[color.rgb.red], points=[p1])
c2 = Circle(center=p2, radius=0.5, fill=[color.rgb.blue], points=[p2])

fd.draw("pyfeyn-test5.pdf")
