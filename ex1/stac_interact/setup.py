#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup_args = dict(
  author="Chris Beddow",
  author_email='christopher.beddow@gmail.com',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
  description="stac_interact package will allow interaction with the STAC API in order to get collections, turn a collection into a dictionary, and count the items in a collection intersecting an input polygon.",
  license="MIT license",
  packages=['stac_interact'],
  install_requires=['json', 'requests','shapely'],
  keywords=['stac','collections','interact'],
  include_package_data=True,
  name='stac_interact',
  version='0.1.0',
  zip_safe=False,
)

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
