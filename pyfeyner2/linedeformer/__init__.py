from pyfeyner2.linedeformer.linedeformer import LineDeformer, Straight
from pyfeyner2.linedeformer.sine import Sine, DoubleSine
from pyfeyner2.linedeformer.coil import Coil


def standard_deformer(name):
    return standard_deformer.table.get(name, None)()

standard_deformer.table = {"straight" : Straight,
                           "sine" : Sine,
                           "doublesine" : DoubleSine,
                           "coil" : Coil}


__all__ = ["LineDeformer", "Straight", "Sine", "DoubleSine", "Coil"]
