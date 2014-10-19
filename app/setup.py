# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import app
version = app.__version__

setup(
    name='test_neo',
    version=version,
    author='',
    author_email='josephmfusaro@gmail.com',
    packages=[
        'app',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['app/manage.py'],
)