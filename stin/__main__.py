# from .solution import run
#
# def main():
#     run()
#
# if __name__ == "__main__":
#     main()

from .solution import run

raw_results = run()
x = run[0]
results = run[1:]
description = ('α_L', 'liquid fraction', 'liquid fraction (α_L), nondimensional'),\
              ('α_G', 'gas fraction', 'gas fraction (α_G), nondimensional'),\
              ('v_L', 'liquid velocity', 'liquid velocity (v_L), m/s'),\
              ('v_G', 'gas velocity', 'gas velocity (v_G), m/s'),\
              ('ρ_G', 'gas density', 'gas denstiy (ρ_G), kg/m^3'),\
              ('p', 'pressure', 'pressure (p), Pa')
def plotting(i):
    plt.figure(description[i][0])
    plt.plot(x, results[i], label=description[i][1])
    plt.xlim( left=100, right=max(x) )
    plt.legend()
    plt.xlabel('wellbore length (x), m')
    plt.ylabel(description[i][2])

if __name__ == "__main__":
    po = Pool(processes=4)
    graphs = po.map(plotting, results)
