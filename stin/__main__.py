from .solution import run, plotting
from multiprocessing import Pool
import argparse
import sys


def main():
    begin = argparse.ArgumentParser(description = 'This program simulates steady \
                                    influx using drift-flux model')
    begin.add_argument('-alpha', '--initial_gas_fraction', type = float, required = True,
                        help = 'specify initial gas influx concentration (start with 0.01)')
    list_of_args = begin.parse_args(sys.argv[1:])
    α_G0 = list_of_args.initial_gas_fraction

    pair = run(α_G0)

    po = Pool(processes=6)
    graphs = po.map(plotting, pair)

if __name__ == '__main__':
    main()
