# For QAPYTH3 Exercises
# python setup.py build
# python setup.py install
# python setup.py bdist_wininst
from distutils.core import setup, Extension

module1 = Extension('getprocs',
                    sources = ['getprocs.c'])

setup (name = 'getprocs',
       version = '1.1',
       description = 'This returns a list of (PID,PPID,EXE) tuples',
       ext_modules = [module1])