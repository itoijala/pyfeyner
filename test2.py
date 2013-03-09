from pyfeyner2.line import Line
from pyfeyner2.diagram import Diagram

l1 = Line((0, 0), (1, 0), color="r", deformer="cycloid")
l1.deformer.is3d = True
l2 = Line((1, 0), (1, 1), color="b", deformer="sine")
l3 = Line((1, 1), (0, 0), color="g", bend=0.1, deformer="cycloid")

d = Diagram()
d.add(l1)
d.add(l2)
d.add(l3)
d.save("a.pdf")
