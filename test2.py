import pyfeyner2.marker
from pyfeyner2.diagram import Diagram
from pyfeyner2.line import Line
from pyfeyner2.point import Point

d = Diagram()
p1 = d.add(Point(-2, 0, marker="circle"))
p2 = d.add(Point(2, 0, marker="circle"))
l1 = d.add(Line((-4, 2), p1))
l2 = d.add(Line((-4, -2), p1))
l3 = d.add(Line(p1, p2, deformer="sine"))
l4 = d.add(Line(p2, (4, 2)))
l5 = d.add(Line(p2, (4, -2)))
l6 = d.add(Line((3, 1), (3, -1), bend=-0.5, deformer="coil"))
l7 = d.add(Line((-3, 1), (-3, -1), bend=0.5, deformer="doublesineline"))
d.save("a.pdf")
