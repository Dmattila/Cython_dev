from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Move cursor library',
    ext_modules=cythonize("movelib.pyx"),
    zip_safe=False,
)