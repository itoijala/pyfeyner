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

"""A couple of classes for decorating diagram elements."""

import math

import pyx

from pyfeyner.diagrams import FeynDiagram
from pyfeyner.utils import Visible
from pyfeyner import config


class Arrow(pyx.deco.deco, pyx.attr.attr):
    """Arrow for Feynman diagram lines"""

    def __init__(self, pos=0.5, size=6*pyx.unit.v_pt,
                 angle=45, constriction=0.8):
        self.pos = pos
        self.size = size
        self.angle = angle
        self.constriction = constriction

    def decorate(self, dp, texrunner=pyx.text.defaulttexrunner):
        """Attach arrow to a path (usually a line)."""
        dp.ensurenormpath()
        constrictionlen = self.size * self.constriction * \
                          math.cos(self.angle * math.pi / 360.0)
        arrowtopos = self.pos * dp.path.arclen() + 0.5 * self.size
        arrowtopath = dp.path.split(arrowtopos)[0]
        arrowpath = pyx.deco._arrowhead(arrowtopath, self.pos*dp.path.arclen(),
                                        1, self.size, 45, True, constrictionlen)
        dp.ornaments.fill(arrowpath)
        return dp


class FreeArrow(Visible):
    """Arrow not attached to any line in a diagram."""

    def __init__(self, length=0.5 * pyx.unit.v_cm, size=6 * pyx.unit.v_pt,
                 angle=45, constriction=0.8, pos=None, x=None, y=None,
                 direction=0):
        self.x, self.y = 0, 0
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if pos is not None:
            self.x, self.y = pos.getXY()
        self.direction = direction
        self.length = length
        self.size = size
        self.angle = angle
        self.constriction = constriction

    def draw(self, canvas):
        """Draw this arrow on the supplied canvas."""
        endx, endy = self.x - self.length * math.sin(self.direction * math.pi / 180.0), \
                     self.y - self.length * math.cos(self.direction * math.pi / 180.0)
        linepath = pyx.deco.decoratedpath(pyx.path.path(pyx.path.moveto(endx, endy),
                                          pyx.path.lineto(self.x, self.y)))
        styles = [pyx.deco.earrow(size=self.size, angle=self.angle,
                        constriction=self.constriction)]
        canvas.stroke(linepath.path, styles)


class ParallelArrow(Visible):
    """Arrow running parallel to a line, for momenta, helicities etc."""

    def __init__(self, line, pos=0.5, displace=0.3, length=0.5 * pyx.unit.v_cm,
                 size=6 * pyx.unit.v_pt, angle=45, constriction=0.8, sense=1,
                 curved=False, stems=1, stemsep=0.03):
        self.line = line
        self.pos = pos
        self.displace = pyx.unit.length(displace)
        self.length = length
        self.size = size
        self.angle = angle
        self.constriction = constriction
        self.sense = sense
        self.curved = curved
        self.stems = stems
        self.stemsep = stemsep

    def draw(self, canvas):
        """Draw this arrow on the supplied canvas."""
        p = self.line.getPath()
        posparam = p.begin() + self.pos * p.arclen()
        x, y = self.line.fracpoint(self.pos).getXY()
        arrx, arry = self.line.fracpoint(self.pos + self.length / 2.0 / p.arclen()).getXY()
        endx, endy = self.line.fracpoint(self.pos - self.length / 2.0 / p.arclen()).getXY()

        # Calculate the displacement from the line
        displacement = self.displace
        intrinsicwidth = pyx.unit.length(0.1)
        if hasattr(self.line, "arcradius"):
            intrinsicwidth = self.line.arcradius
        if displacement > 0:
            displacement += intrinsicwidth
        else:
            displacement -= intrinsicwidth
        if config.DEBUG:
            print "Displacement = ", displacement

        # Position the arrow on the right hand side of lines
        tangent = p.tangent(posparam, displacement)
        normal = tangent.transformed(pyx.trafo.rotate(90, x, y))
        nx, ny = normal.atend()
        nxcm, nycm = pyx.unit.tocm(nx - x), pyx.unit.tocm(ny - y)
        vx, vy = p.atbegin()
        vxcm, vycm = pyx.unit.tocm(x - vx), pyx.unit.tocm(y - vy)

        # If the arrow is on the left, flip it by 180 degrees
        if (vxcm * nycm - vycm * nxcm) > 0:
            normal = normal.transformed(pyx.trafo.rotate(180, x, y))
            nx, ny = normal.atend()
        if displacement < 0:
            normal = normal.transformed(pyx.trafo.rotate(180, x, y))
            nx, ny = normal.atend()

        # Displace the arrow by this normal vector
        endx, endy = endx + (nx - x), endy + (ny - y)
        arrx, arry = arrx + (nx - x), arry + (ny - y)

        if self.sense < 0:
            arrx, arry, endx, endy = endx, endy, arrx, arry

        if not self.curved:
            linepath = pyx.path.path(pyx.path.moveto(endx, endy),
                                     pyx.path.lineto(arrx, arry))
            styles = [pyx.deco.earrow(size=self.size, angle=self.angle,
                                      constriction=self.constriction)]
            dist = self.stemsep
            n = self.stems
            if n > 1:  # helicity style arrow
                arrowtopath = linepath.split(0.8 * linepath.arclen())[0]
                constrictionlen = self.size * self.constriction * \
                                  math.cos(self.angle * math.pi / 360.0)
                arrowpath = pyx.deco._arrowhead(arrowtopath,
                                                linepath.arclen(),
                                                1, self.size, 45,
                                                True, constrictionlen)
                canvas.fill(arrowpath)
                path = pyx.deformer.parallel(-(n + 1) / 2 * dist).deform(arrowtopath)
                defo = pyx.deformer.parallel(dist)
                for m in range(n):
                    path = defo.deform(path)
                    canvas.stroke(path, [])
            else:  # ordinary (momentum) arrow
                canvas.stroke(linepath, styles)
        else:  # curved arrow (always momentum-style)
            curvepiece = self.line.getPath().split([(self.pos*p.arclen()-self.length/2.0),
                                                    (self.pos*p.arclen()+self.length/2.0)])
            arrpiece = curvepiece[1]
            if self.sense < 0:
                arrpiece = arrpiece.reversed()
            linepath = pyx.deco.decoratedpath(pyx.deformer.parallel(displacement).deform(arrpiece))
            styles = [pyx.deco.earrow(size=self.size, angle=self.angle,
                            constriction=self.constriction)]
            canvas.stroke(linepath.path, styles)


class Label(Visible):
    """General label, unattached to any diagram elements"""

    def __init__(self, text, pos=None, x=None, y=None, size=pyx.text.size.normalsize):
        self.x, self.y = 0, 0
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        self.size = size
        self.text = text
        self.textattrs = []
        self.pos = pos

    def draw(self, canvas):
        """Draw this label on the supplied canvas."""
        textattrs = pyx.attr.mergeattrs([pyx.text.halign.center,
                                         pyx.text.vshift.mathaxis,
                                         self.size] + self.textattrs)
        t = pyx.text.defaulttexrunner.text(self.x, self.y, self.text, textattrs)
        canvas.insert(t)


class PointLabel(Label):
    """Label attached to points on the diagram"""

    def __init__(self, point, text, displace=0.3, angle=0, size=pyx.text.size.normalsize):
        self.size = size
        self.displace = pyx.unit.length(displace)
        self.angle = angle
        self.text = text
        self.point = point
        self.textattrs = []

    def getPoint(self):
        """Get the point associated with this label."""
        return self.point

    def setPoint(self, point):
        """Set the point associated with this label."""
        self.point = point
        return self

    def draw(self, canvas):
        """Draw this label on the supplied canvas."""
        x = self.point.getX() + self.displace * math.cos(math.radians(self.angle))
        y = self.point.getY() + self.displace * math.sin(math.radians(self.angle))
        textattrs = pyx.attr.mergeattrs([pyx.text.halign.center,
                                         pyx.text.vshift.mathaxis,
                                         self.size] + self.textattrs)
        t = pyx.text.defaulttexrunner.text(x, y, self.text, textattrs)
        canvas.insert(t)


class LineLabel(Label):
    """Label for Feynman diagram lines"""

    def __init__(self, line, text, pos=0.5, displace=0.3, angle=0, size=pyx.text.size.normalsize):
        self.pos = pos
        self.size = size
        self.displace = pyx.unit.length(displace)
        self.angle = angle
        self.text = text
        self.line = line
        self.textattrs = []

    def getLine(self):
        """Get the associated line."""
        return self.line

    def setLine(self, line):
        """Set the associated line."""
        self.line = line
        return self

    def draw(self, canvas):
        """Draw this label on the supplied canvas."""
        p = self.line.getPath()
        #x, y = self.line.fracPoint(self.pos).getXY()
        posparam = p.begin() + self.pos * p.arclen()
        x, y = p.at(posparam)

        # Calculate the displacement from the line
        displacement = self.displace
        intrinsicwidth = pyx.unit.length(0.1)
        if hasattr(self.line, "arcradius"):
            intrinsicwidth = self.line.arcradius
        if displacement > 0:
            displacement += intrinsicwidth
        else:
            displacement -= intrinsicwidth
        if config.DEBUG:
            print "Displacement = ", displacement

        # Position the label on the right hand side of lines
        tangent = p.tangent(posparam, displacement)
        normal = tangent.transformed(pyx.trafo.rotate(90, x, y))
        nx, ny = normal.atend()
        nxcm, nycm = pyx.unit.tocm(nx - x), pyx.unit.tocm(ny - y)
        vx, vy = p.atbegin()
        vxcm, vycm = pyx.unit.tocm(x - vx), pyx.unit.tocm(y - vy)

        # If the label is on the left, flip it by 180 degrees
        if (vxcm * nycm - vycm * nxcm) > 0:
            normal = normal.transformed(pyx.trafo.rotate(180, x, y))
            nx, ny = normal.atend()
        if displacement < 0:
            normal = normal.transformed(pyx.trafo.rotate(180, x, y))
            nx, ny = normal.atend()

        # Displace the label by this normal vector
        x, y = nx, ny

        textattrs = pyx.attr.mergeattrs([pyx.text.halign.center,
                                         pyx.text.vshift.mathaxis,
                                         self.size] + self.textattrs)
        t = pyx.text.defaulttexrunner.text(x, y, self.text, textattrs)
        #t.linealign(self.displace,
        #            math.cos(self.angle * math.pi/180),
        #            math.sin(self.angle * math.pi/180))
        canvas.insert(t)


__all__ = ["Arrow", "FreeArrow", "ParallelArrow", "Label", "PointLabel", "LineLabel"]
