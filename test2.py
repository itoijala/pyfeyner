from pyfeyner2.line import Line
from pyfeyner2.diagram import Diagram

l1 = Line((0, 0), (5, 0), color="r", deformer="coil")
l1.deformer.parity3d = 1
l1.deformer.extra = 5
l2 = Line((5, 0), (5, 5), color="b", deformer="sine")
l2.deformer.symmetric = False
l3 = Line((5, 5), (0, 0), color="g", bend=1, deformer="coil")
l3.deformer.mirror = True
l4 = Line((10, 10), (10, 10), arcthru=(5, 15), deformer="coil")

d = Diagram()
d.add(l1)
d.add(l2)
d.add(l3)
d.add(l4)
d.save("a.pdf")
