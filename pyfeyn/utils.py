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

"""Utility functions and classes for PyFeyn"""

import pyx
from pyfeyn.diagrams import FeynDiagram
from pyfeyn import config


## Default units
defunit = pyx.unit.cm
todefunit = pyx.unit.tocm


def sign(x):
    """Get the sign of a numeric type"""
    if x < 0:
        return -1
    if x > 0:
        return 1
    if x == 0:
        return 0


class Visible:
    def isVisible(self):
        """Check if this instance is visible."""
        return True

    def getPath(self):
        """Return the path of this instance."""
        return None

    def getVisiblePath(self):
        """Return the visible path of this instance."""
        return self.getPath()

    def setDepth(self, depth):
        """Set the depth at which this instance lives."""
        self.depth = depth
        return self

    def getDepth(self):
        """Return the depth at which this instance lives."""
        if self.__dict__.has_key("depth"):
            return self.depth
        else:
            return None
        
    def __cmp__(self, other):
        """Compare with another visible class, just using layers."""
        if other is None:
            return -1

        if config.getOptions().DEBUG:
            print "Comparing visible classes: ", \
                  self.__class__, "->", self.getDepth(), "vs.", \
                  other.__class__, "->", other.getDepth()
        else:
            return cmp(self.getDepth(), other.getDepth())

