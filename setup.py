#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = ['everett']

test_requirements = ['pytest', 'pytest-watch', 'pytest-cov', 'flake8']

setuptools.setup(
    name = 'configlib',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='tests',
    version = '2.0.1',
    description = 'wrapper for ConfigParser allowing for simple get calls to set options.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jeff Bryner',
    author_email='jeff@jeffbryner.com',
    url="https://github.com/jeffbryner/configlib",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ]
)
