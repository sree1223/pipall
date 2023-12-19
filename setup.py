# setup.py
from setuptools import setup

setup(
    name='pipall',
<<<<<<< HEAD
    version='0.0.6',
=======
    version='0.1',
>>>>>>> 7a6da01e9eacfb4840e296fbe1fc74e995540649
    packages=['pipall'],
    entry_points={
        'console_scripts': [
            'pipall=pipall.installer:main',
        ],
    },
<<<<<<< HEAD
    author="Sree Harsha",
    author_email="sreeharsha120203@gmail.com",
    keywords=["pipall","pythonversions"],
    description="PipAll is a Python library management tool that simplifies the installation, uninstallation, and listing of libraries for different Python versions.",
    long_description="""
# pipall - Python Library Management

PipAll is a Python library management tool that simplifies the installation, uninstallation, and listing of libraries for different Python versions.

## Installation

 - pip install pipall


Install a Library
 - pipall install <library_name>

Replace <library_name> with the name of the library you want to install.


Uninstall a Library
 - pipall uninstall <library_name>

Replace <library_name> with the name of the library you want to uninstall.


List Installed Python Versions
 - pipall pythons


List Libraries under a Python Version
 - pipall listlib


List All Commands
 - pipall help


Example of installing a library:

 - pipall install requests

This will install the requests library for the default Python version.""",
=======
>>>>>>> 7a6da01e9eacfb4840e296fbe1fc74e995540649
)
