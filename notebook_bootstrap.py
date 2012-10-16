from urllib import urlretrieve
# Download ez_setup.py
try:
    from ez_setup import main as setuptools_main
except ImportError:
    urlretrieve("http://peak.telecommunity.com/dist/ez_setup.py", "ez_setup.py")
    from ez_setup import main as setuptools_main

# Install setuptools
setuptools_main([])

# Download pip ?
urlretrieve("http://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz#md5=db8a6d8a4564d3dc7f337ebed67b1a85",
            "pip-1.2.1.tar.gz")

# Install pip
import tarfile

tar = tarfile.open("pip-1.2.1.tar.gz")
tar.extractall()
tar.close()

from os.path import isdir, join

if isdir('C:/Python27'):
    python_command = join("C:", "Python27", "python.exe")
    pip_command = join("C:", "Python27", "Scripts", "pip.exe")
else:
    python_command = "python"
    pip_command = "pip"

from os import chdir
from subprocess import Popen, PIPE
chdir("pip-1.2.1")
handle = Popen(python_command + " setup.py install",
               shell=True, stdout=PIPE, stderr=PIPE)

# Download tornado
handle = Popen(pip_command + " install tornado",
               shell=True, stdout=PIPE, stderr=PIPE)
stdout, stderr = handle.communicate()
print stdout

# Download pyzmq
handle = Popen(pip_command + " install pyzmq",
               shell=True)
stdout, stderr = handle.communicate()
print stdout
