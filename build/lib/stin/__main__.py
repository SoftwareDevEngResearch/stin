from . import solution
from multiprocessing import Pool
# from matplotlib import pyplot as plt



if __name__ == "__main__":
    po = Pool(processes=6)
    graphs = po.map(solution.plotting, solution.results)
