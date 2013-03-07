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

"""
pyfeyner - a simple Python interface for making Feynman diagrams.
"""

version = "0.1"

## Import PyX and set up some things
import pyx

## Units
pyx.unit.set(uscale = 4, vscale = 4, wscale = 4, xscale = 4)
pyx.unit.set(defaultunit = "cm")

## TeX stuff
pyx.text.defaulttexrunner.set(mode="latex")
if pyx.filelocator.kpsewhich().openers("hepnicenames.sty", ["tex"], "", ""):
    pyx.text.defaulttexrunner.preamble(r"\usepackage{hepnicenames}")
else:
    print "Warning: hepnames LaTeX package not found!"

## Set __all__ (for "from pyfeyner import *")
__all__ = ["diagrams", "points", "blobs", "lines", "deco", "utils", "config"]

del pyx
