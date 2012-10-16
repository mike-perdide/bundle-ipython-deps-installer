Bundle installer for IPython 0.13 Notebook Dependencies on Windows
==================================================================

The goal of this project is to have an effortless way to fetch and install all needed dependencies to launch Ipython 0.13 Notebook on potentially unconfigured Windows (meaning we don't have access to pip for instance).

This project starts with very litlle knowledge of how Python works on Windows, but hopefully it will grow into something both efficient and aesthetic. In the meanwhile, bear with me :).

The scripts aims, for now, at Python 2.7.

How to use it
-------------

Install Python 2.7 for Windows: http://www.python.org/getit

Install IPython 0.13 for Windows: http://pypi.python.org/pypi/ipython

Download the bootstrap script, and launch it::

    C:> [path_to_Python27]\python.exe notebook_boostrap.py

Why and where it might be needed
--------------------------------

This idea comes from a friend of mine teaching programmation through Python to high schoolers. Althought he could benefit from the beautiful notebook feature of IPython 0.13, he doesn't have any particular skill with installing Python modules, and has to work with the computers of his students. Therefore, he can't spend 20 minutes or so fetching every dependency, install in the right places and such ...
