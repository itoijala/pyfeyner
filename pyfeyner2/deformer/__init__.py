from pyfeyner2.deformer.deformer import Deformer
from pyfeyner2.deformer.sine import Sine, DoubleSine, SineLine, DoubleSineLine
from pyfeyner2.deformer.coil import Coil, CoilLine


def _standard_deformer(name):
    return _standard_deformer.table.get(name, None)

_standard_deformer.table = {
        "sine" : Sine,
        "doublesine" : DoubleSine,
        "sineline" : SineLine,
        "doublesineline" : DoubleSineLine,
        "coil" : Coil,
        "coilline" : CoilLine,
        }


__all__ = ["Deformer", "Sine", "DoubleSine", "SineLine", "DoubleSineLine", "Coil", "CoilLine"]
