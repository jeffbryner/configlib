#!/usr/bin/env python
from setuptools import setup, find_packages

requirements = ['everett']

test_requirements = ['pytest', 'pytest-watch', 'pytest-cov', 'flake8']

setup(
    name = 'configlib',
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='tests',
    version = '1.0.1',
    description = 'wrapper for ConfigParser allowing for simple get,set,delete calls to set options.',
    author='Jeff Bryner',
    author_email='jeff@jeffbryner.com',
    url="https://github.com/jeffbryner/configlib"
)
