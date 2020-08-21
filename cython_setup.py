from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize('source_c.pyx','source.py',annotate=True))