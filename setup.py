#!/usr/bin/env python

__author__ = 'Xyene'
from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fh:
    long_description = fh.read()

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cube2sphere', 'version.py')) as version:
    exec (version.read())

setup(name='cube2sphere',
      version=__version__,
      description='Utility to map 6 cube (cubemap, skybox) faces into an equirectangular (cylindrical projection, skysphere) map',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Tudor Brindus',
      author_email='me@tbrindus.ca',
      url='http://github.com/Xyene/cube2sphere',
      packages=find_packages(),
      package_data={
          "cube2sphere": ["*.blend"],
      },
      entry_points={
          'console_scripts': ['cube2sphere=cube2sphere.cube2sphere:main'],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Artistic Software'
      ],
)
