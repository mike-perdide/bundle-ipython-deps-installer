import sys
from urllib import urlretrieve
from subprocess import Popen, PIPE
from os.path import isdir, join, basename
from os import chdir

is_64bits = sys.maxsize > 2 ** 32

PIP_URL = "http://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz"
EZ_SETUP_URL = "http://peak.telecommunity.com/dist/ez_setup.py"

if is_64bits:
    ZMQ_URL = "https://github.com/downloads/zeromq/pyzmq/pyzmq-2.2.0.win-amd64-py2.7.msi "
else:
    ZMQ_URL = "https://github.com/downloads/zeromq/pyzmq/pyzmq-2.2.0.win32-py2.7.msi"


def install_pip():
    import tarfile

    # Download pip
    # Md5: #md5=db8a6d8a4564d3dc7f337ebed67b1a85
    urlretrieve(PIP_URL, basename(PIP_URL))

    # Install pip
    tar = tarfile.open(basename(PIP_URL))
    tar.extractall()
    tar.close()

    if isdir('C:/Python27'):
        python_command = join("C:/", "Python27", "python.exe")
    else:
        python_command = "python"

    chdir(PIP_URL.split(".tar.gz")[0])
    Popen(python_command + " setup.py install",
          shell=True, stdout=PIPE, stderr=PIPE)


# Download ez_setup.py
try:
    from ez_setup import main as setuptools_main
except ImportError:
    urlretrieve(EZ_SETUP_URL, basename(EZ_SETUP_URL))
    from ez_setup import main as setuptools_main

# Install setuptools
setuptools_main([])

# Install pip
try:
    from pip.commands import install
except ImportError:
    install_pip()
    from pip.commands import install


def install_distributions(distributions):
    """Thanks to Ralph Bean, https://github.com/ralphbean"""
    command = install.InstallCommand()
    opts, args = command.parser.parse_args()
    # TBD, why do we have to run the next part here twice before actual install
    requirement_set = command.run(opts, distributions)
    requirement_set = command.run(opts, distributions)
    requirement_set.install(opts)

# Install IPython
try:
    import IPython
    print "IPython is installed."
except ImportError:
    print "installing IPython ... ",
    install_distributions(["ipython", ])
    print "installed."

try:
    import tornado
    print "Tornado is installed."
except ImportError:
    print "Installing tornado ... ",
    install_distributions(["tornado", ])
    print "installed."

try:
    import zmq
    print "Pyzmq is installed."
except ImportError:
    print "installing pyzmq ... ",
    urlretrieve(ZMQ_URL, basename(ZMQ_URL))
    handle = Popen(basename(ZMQ_URL), shell=True, stdout=PIPE, stderr=PIPE)
    print handle.communicate()
    print "installed."