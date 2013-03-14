import pyfeyner2.marker
from pyfeyner2.diagram import Diagram
from pyfeyner2.line import Line
import pyfeyner2.point
from pyfeyner2.point import Point
from pyfeyner2.label import Label

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
lab = d.add(Label(r"${x}{y^2_3}$", 30, 0, 1))
l3.add_label("foo")
l6.add_label(Label("gg", angle=0), position=0.5, additional_angle=0)
l4.add_label(Label("gg2", angle=0), position=0.5, left=True)
l4.add_label(Label("gg3", angle=0), start=True)
l4.add_label(Label("gg4", angle=0), end=True)

pl = d.add(Point(0, -1.3, marker="circle"))
pl.add_label(Label("texg", angle=180), angle=0)

d.save("a.pdf")
