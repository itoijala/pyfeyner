#!/usr/bin/env python2

#
# pyfeyner - a simple Python interface for making Feynman diagrams.
# Copyright (C) 2005-2010 Andy Buckley, Georg von Hippel
# Copyright (C) 2013 Ismo Toijala
#
# pyfeyner is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# pyfeyner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with pyfeyner; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from setuptools import setup

longdesc = """pyfeyner is a package which makes drawing Feynman diagrams simple and programmatic.
Feynman diagrams are important constructs in perturbative field theory, so being able to draw them
in a programmatic fashion is important if attempting to enumerate a large number of diagram
configurations is important. The output quality of pyfeyner diagrams (into PDF or EPS formats)
is very high, and special effects can be obtained by using constructs from PyX, which pyfeyner
is based around."""

setup(name = 'pyfeyner',
      version = '0.1',
      author = 'Andy Buckley, Georg von Hippel, Ismo Toijala',
      author_email = 'ismo.toijala@gmail.com',
      url = 'https://github.com/itoijala/pyfeyner',
      description = 'An easy-to-use Python library to help physicists draw Feynman diagrams.',
      long_description = longdesc,
      keywords = 'feynman hep physics particle diagram',
      license = 'GPLv2+',
      packages = ['pyfeyner'],
      install_requires = ['PyX'],
      zip_safe = False,
      classifiers = ['Development Status :: 2 - Per-Alpha',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Topic :: Scientific/Engineering :: Physics',
                    ],
     )
