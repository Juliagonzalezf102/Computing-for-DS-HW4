try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import JGF_CDS_library


def get_requirements(requirements_path='requirem2ents.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='JGF_CDS_library',
    version=JGF_CDS_library.__version__,
    description='Example library',
    author='Julia',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    classifiers=[
        'Programming Language :: Python :: 3.10.7'
    ]
)
