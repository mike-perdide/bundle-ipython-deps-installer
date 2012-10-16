Bundle installer for IPython 0.13 Notebook Dependencies on Windows
==================================================================

The goal of this project is to have an effortless way to fetch and install all needed dependencies to launch Ipython 0.13 Notebook on potentially unconfigured Windows (meaning we don't have access to pip for instance).

This project starts with very litlle knowledge of how Python works on Windows, but hopefully it will grow into something both efficient and aesthetic. In the meanwhile, bear with me :).

The scripts aims, for now, at Python 2.7.

How to use it
-------------

Install Python 2.7 for Windows: http://www.python.org/getit

Download the bootstrap script, and either launch it from a shell (cmd.exe)::

    C:> C:\Python27\python.exe notebook_boostrap.py

Or by right-clicking on the file, "Open with", "Python".

The installer will launch the IPython and the ZMQ installers if they are not installed, so don't panic. Mostly, all you'll have to do is click "Next" a bunch of times. If you're not new to Windows, you should be used to it by now.

Once the installer has finished, you can either launch the notebook with::

    C:> C:\Python27\Scripts\ipython.exe notebook

Or by pasting the line above inside a new Shortcut (on the Desktop for instance, right-click, "Create new shortcut").

Evolutions
----------

In the near future, this script could be replaced by several .exe bundles:
* Python + this script
* Python + IPython + tornado + pyzmq
* the above + matplotlib

Why and where it might be needed
--------------------------------

This idea comes from a friend of mine teaching programmation through Python to high schoolers. Althought he could benefit from the beautiful notebook feature of IPython 0.13, he doesn't have any particular skill with installing Python modules, and has to work with the computers of his students. Therefore, he can't spend 20 minutes or so fetching every dependency, install in the right places and such ...
