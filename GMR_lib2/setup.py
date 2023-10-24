# This is just a test document for the library GMR_lib1

from setuptools import setup

setup(
    name = 'GMR_lib1',
    version = '0.2',
    description = 'A test library for GMR',
    author = 'Guillem Mirabent Rubinat',
    packages = ['GMR_lib1'],
    install_requires = ['numpy', 'matplotlib', 'pandas', 'scikit-learn'],
)