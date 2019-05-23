# Steady gas-liquid flow with influx modeling

![Build Status](https://travis-ci.org/nepomnyi/stin.svg?branch=master) (https://github.com/nepomnyi/stin)

# About
&nbsp;&nbsp;&nbsp;Steady influx modeling package (stin) allows for simulation of steady influx of gas into a vertical steady flow of liquid for a limited range of flow parameters.It is built on drift-flux model.    
&nbsp;&nbsp;&nbsp;This is a python package, so one should have python (with the standart library) installed installed on the computer.

# Installation
## Installation from source
- Download the [package] from GitHub.
- On your computer, from the command line of your choice go to the package root repository.
- In the command line, type in: py setup.py install (this command will install the package with all necessary dependencies).

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
