#!/usr/local/bin/python

# For QAPYTH3 Exercises
# python setup.py build
# python setup.py install
from distutils.core import setup

setup (name = 'getprocs',
       version = '1.0',
       py_modules = ['getprocs'],
       description = 'This returns a list of (PID,PPID,EXE) tuples')
