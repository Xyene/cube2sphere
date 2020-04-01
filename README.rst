cube2sphere |PyPI version| |PyPI|
===========

.. |PyPI version| image:: https://badge.fury.io/py/cube2sphere.svg
   :target: https://pypi.python.org/pypi/cube2sphere
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/cube2sphere.svg
   :target: https://pypi.python.org/pypi/cube2sphere

``cube2sphere`` is a Python script to map 6 cube (cubemap, skybox)
faces into an equirectangular (cylindrical projection, skysphere) map. See also `cube2sphere`_.

Usage
=====

::

    $ cube2sphere -h
    usage: cube2sphere [-h] [-v] [-r <width> <height>] [-R <rx> <ry> <rz>]
                   [-o <path>] [-f <name>] [-b <path>] [-t <count>] [-V]
                   <front> <back> <right> <left> <top> <bottom>

    Maps 6 cube (cubemap, skybox) faces into an equirectangular (cylindrical
    projection, skysphere) map.

    positional arguments:
      <front>               source front cube face filename
      <back>                source back cube face filename
      <right>               source right cube face filename
      <left>                source left cube face filename
      <top>                 source top cube face filename
      <bottom>              source bottom cube face filename

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -r <width> <height>, --resolution <width> <height>
                            resolution for rendered map (defaults to 1024x512)
      -R <rx> <ry> <rz>, --rotation <rx> <ry> <rz>
                            rotation in degrees to apply before rendering map (z
                            is up)
      -o <path>, --output <path>
                            filename for rendered map (defaults to "out")
      -f <name>, --format <name>
                            format to use when saving map, i.e. "PNG" or "TGA"
      -b <path>, --blender-path <path>
                            filename of the Blender executable (defaults to
                            "blender")
      -t <count>, --threads <count>
                            number of threads to use when rendering (1-64)
      -V, --verbose         enable verbose logging

Supported output formats depend on the Blender installation, but will
generally include TGA, IRIS, JPEG, MOVIE, IRIZ, RAWTGA, AVIRAW, AVIJPEG, PNG,
BMP, and FRAMESERVER.

``cube2sphere`` can be run in a headless environment (e.g., a
server).

Examples
========

If we wanted to stitch 6 cube faces named ``${face}.jpg`` into a 2048x1024 TGA equirectangular map, we could use the following command:

::

    $ cube2sphere front.jpg back.jpg right.jpg left.jpg top.jpg bottom.jpg -r 2048 1024 -fTGA -ostitched

This would generate ``stitched.tga`` in the working directory.

Installation
============

``cube2sphere`` can be easily installed with ``pip``. It requires a Python 3 installation.

It assumes that Blender is installed and the ``blender`` executable is listed in the system PATH environment variable. If it is not possible for PATH to be edited (as in the case of an unprivileged user), the path to the ``blender`` executable may instead be passed through the ``-b`` flag.

Windows
-------

Install `Blender`_, and add ``blender.exe`` to ``PATH``. Finally,

::

    pip install cube2sphere

Linux
-----

::

    $ apt-get install blender
    $ pip install cube2sphere

Mac OS X
--------

Similar to Windows, install `Blender`_, and add the ``blender`` executable to ``$PATH``. Then,

::

    $ pip install cube2sphere

.. _cube2sphere: https://github.com/Xyene/cube2sphere
.. _Blender: https://www.blender.org/
