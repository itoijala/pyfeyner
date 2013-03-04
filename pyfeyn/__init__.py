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

"""
PyFeyn - a simple Python interface for making Feynman diagrams.
"""

__author__ = "Andy Buckley & Georg von Hippel (pyfeyn@projects.hepforge.org)"
__version__ = "0.3.2"
__date__ = "$Date$"
__copyright__ = "Copyright (c) 2007 Andy Buckley"
__license__ = "GPL"


## Import PyX and set up some things
try:
    import pyx

    ## Check the version
    from distutils.version import StrictVersion as Version
    if Version(pyx.version.version) < Version("0.9.0"):
        print "Warning: PyFeyn may not work with PyX versions older than 0.9!"

    ## Units
    pyx.unit.set(uscale = 4, vscale = 4, wscale = 4, xscale = 4)
    pyx.unit.set(defaultunit = "cm")

    ## TeX stuff
    pyx.text.defaulttexrunner.set(mode="latex")
    if pyx.filelocator.kpsewhich().openers("hepnicenames.sty", ["tex"], "", ""):
        pyx.text.defaulttexrunner.preamble(r"\usepackage{hepnicenames}")
    else:
        print "Warning: hepnames LaTeX package not found!"

    ## Set __all__ (for "from pyfeyn import *")
    __all__ = ["diagrams", "points", "blobs", "lines", "deco", "utils", "config"]
except:
    print "You don't have PyX - that's a problem unless you're just running the setup script."
