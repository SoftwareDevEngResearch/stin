# stin v0.2.1

[![Build Status](https://travis-ci.org/nepomnyi/stin.svg?branch=master)](https://travis-ci.org/nepomnyi/stin)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3243702.svg)](https://doi.org/10.5281/zenodo.3243702)

# About
&nbsp;&nbsp;&nbsp;Steady influx modeling package (stin) allows for simulation of steady influx of gas into a vertical steady flow of liquid for a limited range of flow parameters. It is built on drift-flux model.    
&nbsp;&nbsp;&nbsp;This is a python package, so one should have python (with the standard library) installed on the computer. Required python version is 3.7 or newer.
&nbsp;&nbsp;&nbsp;The package has a [documentation website]. It is worth mentioning, that the [documentation website] is still under construction and currently has bad readability. Therefore, it is recommended to use this documentation file along with [the report] for the purpose of the package exploration. As soon as the [documentation website] is updated, this paragraph will notify users about that.
To date, one can find mathematical description of the package along with the software description in [the report].

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
    **pip install <path to the package's root directory>**   
    E.g. for windows:  
    **pip install C:\Users\your_user_name\Documents\stin**  
    In this example, stin is the root directory of the package: the one which contains setup.py file.
    - In order to uninstall the package, from command line of your choice, being in any directory (it doesn't matter), type in:  
    **pip uninstall stin**


## Installation from TestPyPI
- In the command line of your choice (in any directory - it doesn't matter), type in:  
**pip install -i https://test.pypi.org/simple/ stin**
- To uninstall the package use:  
**pip uninstall stin**

# Getting started
Let's consider usage of the package on the example.
- In command line (being in any directory - it doesn't matter) type in: **py -m stin -alpha 0.01**:
    - alternatively, it can be run as: **py -m stin --initial_gas_fraction 0.01**,
    - -m runs the package as a module,
    - -alpha (or --initial_gas_fraction) is a variable that the package takes to run the code - it is influx's initial volume fraction,
    - 0.01 is the value of the variable: can be anything from 0 to 1 not including the extremes:
      - for the zeroth version of the package it is not recommended to specify initial gas fraction values more than 0.4.
- The output is a set of graphs for each flow variable with relation to the length of the vertical pipe,
    - the flow variables are velocities of gas and liquid phases, volume fractions of gas and liquid phases, gas phase density, flow pressure - their distributions along the flow is the output of the software,
    - one may find plots for the current example with explanation in the section 4 of [the report].

# Testing
- Using installation from source:
    - In command line, being in the root directory of the package, type in: **pytest** or **pytest -vv --cov=./**
    - In both cases the result is the same: a user will see two tables
        - the first one will contain names of the unit and integration tests and passing marks to the right of them,
        - the second one will contain test coverage,
        - test coverage for the package is 82%:
            - test coverage doesn't work in TravisCI, that is why continuous integration status badge at the top of this file shows *failing* - fixing this issue entails rewriting a chunk of code and is considered to be a part of future work,
            - integration tests are not written for the plotting function, that is why test coverage is 82% only; writing tests for the plotting function is above the author's knowledge, hence, is considered to be time consuming and left for the future work.
- Using installation from TestPyPI:
    - the author is not aware of any way to apply either *pytest* or *pytest-cov* on an installed package,
    - testing can be done only from within package's root directory - for that purpose the package should be downloaded from GitHub and the above described procedure can be implemented.


# Acknowledgment
[FRIDGe], that helped me to set TravisCI up.

[FRIDGe]: https://github.com/SoftwareDevEngResearch/FRIDGe
[package]: https://github.com/SoftwareDevEngResearch/stin
[documentation website]: https://nepomnyi.github.io/stin/
[the report]: https://github.com/SoftwareDevEngResearch/course-projects-s2019/blob/master/reports/Nepomnyashchikh-project-report.pdf
