#!/usr/bin/env python
#coding: utf8

"""
Setup script for XPCS-tools.
"""

from glob import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='xpcs-tools',
      version='0.0.1',
      author="Fivos Perakis",
      author_email="f.perakis@fysik.su.se",
      url='https://github.com/fperakis/XPCS-tools',
      description='Collection to analyse x-ray photon correlation spectroscopy data',
      packages=["xpcstools"],
      package_dir={'xpcstools': 'src'},
      #install_requires=['scikit-beam', 'scikit-image']
      #scripts=[s for s in glob('scripts/*') if not s.endswith('__.py')],
      #test_suite="test"
      )
