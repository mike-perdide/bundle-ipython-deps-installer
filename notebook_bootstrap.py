from urllib import urlretrieve


def install_pip():
    from os.path import isdir, join
    from os import chdir
    from subprocess import Popen, PIPE
    import tarfile

    # Download pip
    # Md5: #md5=db8a6d8a4564d3dc7f337ebed67b1a85
    urlretrieve(
        "http://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz",
        "pip-1.2.1.tar.gz")

    # Install pip
    tar = tarfile.open("pip-1.2.1.tar.gz")
    tar.extractall()
    tar.close()

    if isdir('C:/Python27'):
        python_command = join("C:", "Python27", "python.exe")
    else:
        python_command = "python"

    chdir("pip-1.2.1")
    Popen(python_command + " setup.py install",
          shell=True, stdout=PIPE, stderr=PIPE)


# Download ez_setup.py
try:
    from ez_setup import main as setuptools_main
except ImportError:
    urlretrieve("http://peak.telecommunity.com/dist/ez_setup.py",
                "ez_setup.py")
    from ez_setup import main as setuptools_main

# Install setuptools
setuptools_main([])

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
    print "Installing pyzmq ... ",
    install_distributions(["pyzmq", ])
    print "installed."
