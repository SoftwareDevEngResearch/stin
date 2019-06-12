from .solution import run, plotting
from multiprocessing import Pool
import argparse
import sys


def main():
    begin = argparse.ArgumentParser(description = 'This software simulates steady \
                                    influx using drift-flux model. You may find \
                                    documentation on this software at \
                                    https://github.com/SoftwareDevEngResearch/stin/blob/master/README.md \
                                    or at https://nepomnyi.github.io/stin/')
    begin.add_argument('-alpha', '--initial_gas_fraction', type = float, required = True,
                        help = 'Specify initial gas influx concentration (start with 0.01 \
                        do not use values more than 0.4, do not use 0). For that \
                        purpose you can use either -alpha or --initial_gas_fraction. \
                        E.g.: py -m stin -alpha 0.01      or      py -m stin --initial_gas_fraction 0.2. \
                        As an output you will receive 6 plots of flow parameters \
                        versus spatial coordinate.')
    list_of_args = begin.parse_args(sys.argv[1:])
    α_G0 = list_of_args.initial_gas_fraction

    pair = run(α_G0)

    po = Pool(processes=6)
    graphs = po.map(plotting, pair)

if __name__ == '__main__':
    main()
