#
# PyFeyn - a simple Python interface for making Feynman diagrams.
# Copyright (C) 2005-2010 Andy Buckley, Georg von Hippel
#
# PyFeyn is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PyFeyn is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with PyFeyn; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

"""Convenience imports for colouring etc."""

import pyx

## Colours
BLACK = pyx.color.rgb.black
BLUE = pyx.color.rgb.blue
GREEN = pyx.color.rgb.green
RED = pyx.color.rgb.red
WHITE = pyx.color.rgb.white
APRICOT = pyx.color.cmyk.Apricot
AQUAMARINE = pyx.color.cmyk.Aquamarine
BITTERSWEET = pyx.color.cmyk.Bittersweet
BLACK = pyx.color.cmyk.Black
BLUE = pyx.color.cmyk.Blue
BLUEGREEN = pyx.color.cmyk.BlueGreen
BLUEVIOLET = pyx.color.cmyk.BlueViolet
BRICKRED = pyx.color.cmyk.BrickRed
BROWN = pyx.color.cmyk.Brown
BURNTORANGE = pyx.color.cmyk.BurntOrange
CADETBLUE = pyx.color.cmyk.CadetBlue
CARNATIONPINK = pyx.color.cmyk.CarnationPink
CERULEAN = pyx.color.cmyk.Cerulean
CORNFLOWERBLUE = pyx.color.cmyk.CornflowerBlue
CYAN = pyx.color.cmyk.Cyan
DANDELION = pyx.color.cmyk.Dandelion
DARKORCHID = pyx.color.cmyk.DarkOrchid
EMERALD = pyx.color.cmyk.Emerald
FORESTGREEN = pyx.color.cmyk.ForestGreen
FUCHSIA = pyx.color.cmyk.Fuchsia
GOLDENROD = pyx.color.cmyk.Goldenrod
GRAY = pyx.color.cmyk.Gray
GREEN = pyx.color.cmyk.Green
GREENYELLOW = pyx.color.cmyk.GreenYellow
GREY = pyx.color.cmyk.Grey
JUNGLEGREEN = pyx.color.cmyk.JungleGreen
LAVENDER = pyx.color.cmyk.Lavender
LIMEGREEN = pyx.color.cmyk.LimeGreen
MAGENTA = pyx.color.cmyk.Magenta
MAHOGANY = pyx.color.cmyk.Mahogany
MAROON = pyx.color.cmyk.Maroon
MELON = pyx.color.cmyk.Melon
MIDNIGHTBLUE = pyx.color.cmyk.MidnightBlue
MULBERRY = pyx.color.cmyk.Mulberry
NAVYBLUE = pyx.color.cmyk.NavyBlue
OLIVEGREEN = pyx.color.cmyk.OliveGreen
ORANGE = pyx.color.cmyk.Orange
ORANGERED = pyx.color.cmyk.OrangeRed
ORCHID = pyx.color.cmyk.Orchid
PEACH = pyx.color.cmyk.Peach
PERIWINKLE = pyx.color.cmyk.Periwinkle
PINEGREEN = pyx.color.cmyk.PineGreen
PLUM = pyx.color.cmyk.Plum
PROCESSBLUE = pyx.color.cmyk.ProcessBlue
PURPLE = pyx.color.cmyk.Purple
RAWSIENNA = pyx.color.cmyk.RawSienna
RED = pyx.color.cmyk.Red
REDORANGE = pyx.color.cmyk.RedOrange
REDVIOLET = pyx.color.cmyk.RedViolet
RHODAMINE = pyx.color.cmyk.Rhodamine
ROYALBLUE = pyx.color.cmyk.RoyalBlue
ROYALPURPLE = pyx.color.cmyk.RoyalPurple
RUBINERED = pyx.color.cmyk.RubineRed
SALMON = pyx.color.cmyk.Salmon
SEAGREEN = pyx.color.cmyk.SeaGreen
SEPIA = pyx.color.cmyk.Sepia
SKYBLUE = pyx.color.cmyk.SkyBlue
SPRINGGREEN = pyx.color.cmyk.SpringGreen
TAN = pyx.color.cmyk.Tan
TEALBLUE = pyx.color.cmyk.TealBlue
THISTLE = pyx.color.cmyk.Thistle
TURQUOISE = pyx.color.cmyk.Turquoise
VIOLET = pyx.color.cmyk.Violet
VIOLETRED = pyx.color.cmyk.VioletRed
WHITE = pyx.color.cmyk.White
WILDSTRAWBERRY = pyx.color.cmyk.WildStrawberry
YELLOW = pyx.color.cmyk.Yellow
YELLOWGREEN = pyx.color.cmyk.YellowGreen
YELLOWORANGE = pyx.color.cmyk.YellowOrange

## Patterns
CROSSHATCHED0 = pyx.pattern.crosshatched(0.1, 0) 
CROSSHATCHED45 = pyx.pattern.crosshatched(0.1, 45)
HATCHED0 = pyx.pattern.hatched0
HATCHED45 = pyx.pattern.hatched45
HATCHED90 = pyx.pattern.hatched90
HATCHED135 = pyx.pattern.hatched135

## Line widths
THICK6 = pyx.style.linewidth.THICK 
THICK5 = pyx.style.linewidth.THICk 
THICK4 = pyx.style.linewidth.THIck 
THICK3 = pyx.style.linewidth.THick 
THICK2 = pyx.style.linewidth.Thick 
THICK1 = pyx.style.linewidth.thick 
NORMAL = pyx.style.linewidth.normal
THIN1 = pyx.style.linewidth.thin
THIN2 = pyx.style.linewidth.Thin
THIN3 = pyx.style.linewidth.THin
THIN4 = pyx.style.linewidth.THIn
THIN5 = pyx.style.linewidth.THIN
CLEAR = pyx.style.linewidth.clear
