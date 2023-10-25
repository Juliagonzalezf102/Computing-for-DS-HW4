from setuptools import setup, find_packages

setup(
    name='jolibhw4',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'random'
    ],
)