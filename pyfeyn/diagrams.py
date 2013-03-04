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

"""Classes for the actual diagram containers."""

import pyx
from pyfeyn import config


## Diagram class
class FeynDiagram:
    """The main PyFeyn diagram class."""    
    currentDiagram = None

    def __init__(self, objects=None, canvas=None):
        """Objects for holding a set of Feynman diagram components."""
        self.__objs = objects
        if self.__objs is None:
            self.__objs = []
        self.highestautolayer = 0
        if canvas is None:
           self.currentCanvas = pyx.canvas.canvas()
        else:
           self.currentCanvas = canvas
        FeynDiagram.currentDiagram = self


    def add(self, *objs):
        """Add an object to the diagram."""
        for obj in objs:
            if config.getOptions().DEBUG:
                print "#objs = %d" % len(self.__objs)
            offset = 0
            if obj.__dict__.has_key("layeroffset"):
                #print "offset =", obj.layeroffset
                offset = obj.layeroffset
            self.highestautolayer += 1
            obj.setDepth(self.highestautolayer + offset)
            if config.getOptions().DEBUG:
                print "Object %s layer = %d + %d = %d" % \
                      (obj.__class__, self.highestautolayer, offset,
                       self.highestautolayer + offset)
            self.__objs.append(obj)


    def drawToCanvas(self):
        """Draw the components of this diagram in a well-defined order."""
        if config.getOptions().DEBUG:
            print "Final #objs = %d" % len(self.__objs)
        if config.getOptions().VDEBUG:
            print "Running in visual debug mode"

        ## Sort drawing objects by layer
        drawingobjs = self.__objs
        try:
            drawingobjs.sort()
        except:
            pass
            
        ## Draw each object
        for obj in drawingobjs:
            if config.getOptions().DEBUG:
                print "Depth = ", obj.getDepth()
            obj.draw(self.currentCanvas)

        return self.currentCanvas


    def draw(self, outfile):
        """Draw the diagram to a file, with the filetype (EPS or PDF)
        derived from the file extension."""
        c = self.drawToCanvas()
        if c is not None and outfile is not None:
            c.writetofile(outfile)

