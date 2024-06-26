from distutils.core import setup
from glob import glob

setup(name = "PyDealerPickcard",
      version = "1.0",
      author = "QA",
      author_email = "QA.com",
      py_modules = ['libcard'],
      packages = ['Showcard'],
      scripts = ['simple.py','dealer.py'],
      data_files = [('Bitmaps',glob('Bitmaps/*')),
                    ('.', ['qa.ico'])],
      )
      
""" pythopn setup.py sdist
running sdist
running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: either (author and author_email) or (maintain
r and maintainer_email) must be supplied

warning: sdist: manifest template 'MANIFEST.in' does not exist (using default fi
e list)
"""