**DEPRECATED:** Consider using [my fork of dmenu](https://github.com/RyanMcG/dmenu) instead.

============
center_dmenu
============
------------------------
A script to center dmenu
------------------------

:Author: Ryan McGowan
:Email: ryan@ryanmcg.com

Introduction
------------

A simple script to center dmenu.

**NOTE:** This does not have good behaviour for multiple monitors yet.

.. image:: http://i.imgur.com/goITZ.png

Running *center_dmenu* / Installation
----------------------------------

**NOTE:** Python 3 is not supported since `python-xlib` is not available for
python 3.

*center_dmenu* is available via pip. ::

    pip2 install center_dmenu

To install center_dmenu from source: ::

    git clone git://github.com/RyanMcG/center_dmenu.git
    cd center_dmenu
    python2 setup.py install

You probably also need the `python-xlib` package. It is hard to get this via
pip so just use your package manager. ::

    sudo apt-get install python-xlib # In ubuntu

If you want to run center_dmenu from source you need to manually get the
dependencies first. ::

    # Assuming you are already in the center_dmenu directory
    pip2 install -r requirements.txt

Usage
-----

::

    center_dmenu [margin] [height] [extra_dmenu_args]

TODO
~~~~
-   Make it work for multiple monitors (query Outputs instead of screens?)
-   Improve README
