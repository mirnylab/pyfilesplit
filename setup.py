#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

classifiers = """\
    Development Status :: 4 - Beta
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
"""

setup(
    name='pyfilesplit',
    author='Mirny Lab',
    author_email='espresso@mit.edu',
    version='0.1.0',
    license='MIT',
    description='A simple command line tool to split files into chunks.',
    long_description=('Split a file into pieces in a round robin fashion. '
                'Covers the missing functionality of GNU split by enabling '
                'multi-line round robin splits.'),
    url='https://github.com/mirnylab/pyfilesplit',
    packages=['pyfilesplit'],
    zip_safe=False,
    scripts=['pyfilesplit/pyfilesplit'],

)
