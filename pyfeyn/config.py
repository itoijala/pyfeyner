#
# PyFeyn - a simple Python interface for making Feynman diagrams.
# Copyright (C) 2007 Andy Buckley
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

"""Handle runtime options and command line option parsing."""

from optparse import OptionParser 


def addPyfeynOptions(parser):
    """Add the PyFeyn options to the options parser's option set."""
    parser.add_option("-V", "--visual-debug", dest="VDEBUG", action = "store_true",
                      default = False, help="produce visual debug output")
    parser.add_option("-D", "--debug", dest="DEBUG", action = "store_true",
                      default = False, help="produce debug output")
    parser.add_option("-d", "--draft", dest="DRAFT", action = "store_true",
                      default = False, help="produce draft output, skipping time-consuming calculations")
    return parser


def processOptions(parser=None):
    """Process the given options."""
    global _opts
    if parser is None:
        parser = OptionParser()
        addPyfeynOptions(parser)
    (_options, _args) = parser.parse_args()
    _opts = _options
    return _options, _args


class OptionSet:
    """A container for options."""
    def __init__(self):
        self.DEBUG = False
        self.VDEBUG = False
        self.DRAFT = False


_opts = OptionSet()


def getOptions():
    """Return the (unique) option set."""
    return _opts
