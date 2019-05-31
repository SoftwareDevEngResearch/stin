from . import solution
from multiprocessing import Pool


def main():
    po = Pool(processes=6)
    graphs = po.map(solution.plotting, solution.results)

if __name__ == "__main__":
    main()
