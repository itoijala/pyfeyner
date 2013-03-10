from pyfeyner2.linedeformer.linedeformer import LineDeformer, Straight
from pyfeyner2.linedeformer.sine import Sine, DoubleSine, SineLine
from pyfeyner2.linedeformer.coil import Coil, CoilLine


def standard_deformer(name):
    return standard_deformer.table.get(name, None)()

standard_deformer.table = {"straight" : Straight,
                           "sine" : Sine,
                           "doublesine" : DoubleSine,
                           "sineline" : SineLine,
                           "coil" : Coil,
                           "coilline" : CoilLine,
                          }


__all__ = ["LineDeformer", "Straight", "Sine", "DoubleSine", "SineLine", "Coil", "CoilLine"]
