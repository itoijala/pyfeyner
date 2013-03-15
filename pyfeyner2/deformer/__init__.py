from pyfeyner2.deformer.deformer import Deformer, Straight
from pyfeyner2.deformer.sine import Sine, DoubleSine, SineLine, DoubleSineLine
from pyfeyner2.deformer.coil import Coil, CoilLine


def standard_deformer(name):
    return standard_deformer.table.get(name, None)()

standard_deformer.table = {"straight" : Straight,
                           "sine" : Sine,
                           "doublesine" : DoubleSine,
                           "sineline" : SineLine,
                           "doublesineline" : DoubleSineLine,
                           "coil" : Coil,
                           "coilline" : CoilLine,
                          }


__all__ = ["Deformer", "Straight", "Sine", "DoubleSine", "SineLine", "DoubleSineLine", "Coil", "CoilLine"]
