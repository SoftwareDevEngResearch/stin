from . import solution
from multiprocessing import Pool

if __name__ == "__main__":
    po = Pool(processes=6)
    graphs = po.map(solution.plotting, solution.results)
