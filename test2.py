import pyfeyner2.marker
from pyfeyner2.diagram import Diagram
from pyfeyner2.line import Line
import pyfeyner2.point
from pyfeyner2.label import Label
import pyfeyner2.marker as marker
import pyfeyner2.blob as blob

d = Diagram()
p1 = d.add(marker.Ellipse((-2, 0)))
p2 = d.add(marker.Ellipse((2, 0)))
l1 = d.add(Line((-4, 2), (-2, 0)))
l2 = d.add(Line((-4, -2), (-2, 0)))
l3 = d.add(Line((-2, 0), (2, 0), deformer="sine"))
l4 = d.add(Line((2, 0), (4, 2)))
l5 = d.add(Line((2, 0), (4, -2)))
l6 = d.add(Line((3, 1), (3, -1), bend=-0.5, deformer="coil"))
l7 = d.add(Line((-3, 1), (-3, -1), bend=0.5, deformer="doublesineline"))
lab = d.add(Label(r"${x}{y^2_3}$", 30, (0, 1)))
l3.label("foo")
l6.label(Label("gg", angle=0), position=0.5, additional_angle=0)
l4.label(Label("gg2", angle=0), position=0.5, left=True)
l4.label(Label("gg3", angle=0), start=True)
l4.label(Label("gg4", angle=0), end=True)

pl = d.add(marker.Ellipse((0, -1.3), yscale=3).label(Label("texg", angle=180), angle=0))

d.add(marker.Asterisk((-1, -1), rays=4, angle=45))
d.add(marker.Dummy((-1, 1)).label("bar"))

d.add(blob.Ellipse((1, 1), yscale=2))

d.save("a.pdf")
