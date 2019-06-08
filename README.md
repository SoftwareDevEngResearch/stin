# Steady gas-liquid flow with influx modeling

[![Build Status](https://travis-ci.org/nepomnyi/stin.svg?branch=master)](https://travis-ci.org/nepomnyi/stin)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# About
&nbsp;&nbsp;&nbsp;Steady influx modeling package (stin) allows for simulation of steady influx of gas into a vertical steady flow of liquid for a limited range of flow parameters. It is built on drift-flux model.    
&nbsp;&nbsp;&nbsp;This is a python package, so one should have python (with the standard library) installed on the computer.  
&nbsp;&nbsp;&nbsp;The package has a [documentation website].

# Installation
## Installation from source
- Download the [package] from GitHub. Then there are 2 options.
- *1st option*:
    - On your computer, from the command line of your choice, go to the package root repository.
    - In the command line, type in:  
    **py setup.py install**  
    (this command will install the package with all necessary dependencies).
    - In this case, the package can only be uninstalled manually. For Windows go to **C:\Users\your_user_name\AppData\Local\Continuum\anaconda3\Lib\site-packages\**  
    There you may find a folder called **stin-0.2.0-py3.7.egg** (the folder name may vary dependently on the package version and version of python you use). Delete this folder and the package will be deleted.  
    Note that AppData is a hidden folder.  
    For OSX and Linux the process of uninstallation was not tested.
- *2nd option*:
    - On your computer, from the command line of your choice, being in any directory (it doesn't matter), type in:  
    **pip install <path to the project's directory>**   
    E.g. for windows:  
    **pip install C:\Users\your_user_name\Documents\stin**  
    In this example, stin is the root directory of the package: the one which contains setup.py file.
    - In order to uninstall the package, from command line of your choice, being in any directory (it doesn't matter), type in:  
    **pip uninstall stin**


## Installation from TestPyPI
- In the command line of your choice (in any directory - it doesn't matter), type in:  
**py -m pip -i https://test.pypi.org/simple/ stin**
- To uninstall the package use:  
**pip uninstall stin**

# Getting started
- In command line (being in any directory - it doesn't matter) type in: py -m stin -alpha 0.01:
    - -m runs the package as a module,
    - -alpha is a variable that the package takes to run the code,
    - 0.01 is the value of the variable: can be anything from 0 to 1 not including the extremes.
- The package can also be imported from within python but it is a pointless action since the package requires user's input from command line.
- The output is a set of graphs of each flow parameter with relation to the length of the vertical pipe.

# Acknowledgment
[FRIDGe], that helped me to set TravisCI up.

[FRIDGe]: https://github.com/SoftwareDevEngResearch/FRIDGe
[package]: https://github.com/SoftwareDevEngResearch/stin
[documentation website]: https://nepomnyi.github.io/stin/
