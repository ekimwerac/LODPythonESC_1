# For QAPYTH3 Exercises
# python setup.py build
# python setup.py install
# python setup.py bdist_wininst
from distutils.core import setup
import glob

setup (name = 'showcard',
       version = '1.1',
       description = 'Displays a playing card',
       py_modules = ['showcard'],
       data_files = [
          ('Bitmaps',glob.glob('Bitmaps/*')),
          ('.', ['qa.ico'])]
       )