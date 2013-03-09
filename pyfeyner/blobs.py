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

"""Various blob shapes to represent generic interactions."""

import pyx

from pyfeyner.diagrams import FeynDiagram
from pyfeyner.points import Point
from pyfeyner.utils import Visible
from pyfeyner.deco import PointLabel
from pyfeyner import config


class Blob(Point, Visible):
    """Base class for all blob-like objects in Feynman diagrams"""

    def __init__(self):
        """Dysfunctional constructor, since this is an abstract base class."""
        self.trafos = []
        self.strokestyles = []
        self.fillstyles = []
        self.layeroffset = 1000

    def setStrokeStyle(self, strokestyle):
        """Set the stroke style."""
        self.strokestyles = [strokestyle]
        return self

    def clearStrokeStyles(self):
        """Remove all the current stroke styles."""
        self.strokestyles = []
        return self

    def setFillStyle(self, fillstyle):
        """Set the fill style."""
        self.fillstyles = [fillstyle]
        return self

    def clearFillStyles(self):
        """Remove all the current fill styles."""
        self.fillstyles = []
        return self

    def addTrafo(self, trafo):
        """Add a transformation."""
        self.trafos.append(trafo)
        return self

    def clearTrafos(self):
        """Remove transformations."""
        self.trafos = []
        return self

    def setPoints(self, points):
        """Set the points to which this blob is attached."""
        if points:
            self.points = points
            for p in self.points:
                p.blob = self
        else:
            self.points = []

    def addLabel(self, text, displace=-0.15, angle=0,
                 size=pyx.text.size.normalsize):
        """Add a label."""
        if config.DEBUG:
            print "Adding label: " + text
        self.labels.append(PointLabel(text=text,
                                      point=self,
                                      displace=displace,
                                      angle=angle,
                                      size=size))
        if config.DEBUG:
            print "Labels = " + str(self.labels)
        return self

    def clearLabels(self):
        """Remove all current labels."""
        self.labels = []
        return self


class Circle(Blob):
    """A circular blob"""

    def __init__(self,
                 x=None,
                 y=None,
                 center=None,
                 radius=None,
                 fill=[pyx.color.rgb.white],
                 stroke=[pyx.color.rgb.black],
                 points=None):
        if radius:
            self.radius = float(radius)
        else:
            raise Exception("No (or zero) radius specified for blob.")

        if x is not None and y is not None:
            self.setXY(x, y)
        elif center is not None:
            self.setXY(center.getX(), center.getY())
        else:
            raise Exception("No center specified for blob.")

        self.setPoints(points)
        self.fillstyles = fill
        self.strokestyles = stroke
        self.layeroffset = 1000
        self.trafos = []
        self.labels = []

    def getPath(self):
        """Get the path of this circle blob."""
        return pyx.path.circle(self.getX(), self.getY(), self.radius)

    def draw(self, canvas):
        """Draw this circle blob."""
        canvas.fill(self.getPath(), [pyx.color.rgb.white])
        canvas.fill(self.getPath(), self.fillstyles)
        canvas.stroke(self.getPath(), self.strokestyles)
        for l in self.labels:
            l.draw(canvas)


class Ellipse(Blob):
    "An elliptical blob"

    def __init__(self,
                 x=None,
                 y=None,
                 center=None,
                 xradius=None,
                 yradius=None,
                 fill=[pyx.color.rgb.white],
                 stroke=[pyx.color.rgb.black],
                 points=None):
        self.layeroffset = 1000

        if x is not None and y is not None:
            self.setXY(x, y)
        elif center is not None:
            self.setXY(center.getX(), center.getY())
        else:
            raise Exception("No center specified for blob.")

        self.xrad = None
        if xradius:
            self.setXRadius(xradius)
        elif yradius:
            self.setXRadius(yradius)
        else:
            raise Exception("No viable candidate for x-radius")
        self.yrad = None
        if yradius:
            self.setYRadius(yradius)
        elif xradius:
            self.setYRadius(xradius)
        else:
            raise Exception("No viable candidate for y-radius")

        self.setPoints(points)
        self.fillstyles = fill
        self.strokestyles = stroke
        self.trafos = []
        self.labels = []

    def getXRadius(self):
        """Get the component of the radius in the x-direction."""
        return self.xrad

    def setXRadius(self, xrad):
        """Set the component of the radius in the x-direction."""
        self.xrad = float(xrad)
        return self

    def getYRadius(self):
        """Get the component of the radius in the y-direction."""
        return self.yrad

    def setYRadius(self, yrad):
        """Set the component of the radius in the y-direction."""
        self.yrad = float(yrad)
        return self

    def getXYRadius(self):
        """Get the components of the radius in the x and y
        directions at the same time."""
        return self.getXRadius(), self.getYRadius()

    def setXYRadius(self, xrad, yrad):
        """Get the components of the radius in the x and y
        directions at the same time."""
        self.setXRadius(xrad)
        self.setYRadius(yrad)
        return self

    def getPath(self):
        """Get the path for this blob."""
        ucircle = pyx.path.circle(self.xpos, self.ypos, 1.0)
        mytrafo = pyx.trafo.scale(self.xrad, self.yrad, self.xpos, self.ypos)
        epath = ucircle.transformed(mytrafo)
        return epath

    def draw(self, canvas):
        """Draw this blob on the given canvas."""
        canvas.fill(self.getPath(), [pyx.color.rgb.white])
        canvas.fill(self.getPath(), self.fillstyles)
        #canvas.stroke(self.getPath(), [pyx.color.rgb.white])
        canvas.stroke(self.getPath(), self.strokestyles)
        for l in self.labels:
            l.draw(canvas)


__all__ = ["Blob", "Circle", "Ellipse"]
