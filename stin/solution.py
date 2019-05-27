from .functions import single_v_L, single_p, derivative_p, ρ_G, derivative_v_G, \
                       derivative_α_G, α_L, derivative_v_L, cond
from .boundary_conditions import BC
from importlib import resources
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import yaml

def run():
    """
       At first, the analytical solution for a single-phase flow is used to find pressure
       and velocity of liquid at the point where gas influx occurs.
       At second, system of equation describing gas-liquid flow will be solved numerically
       via explicit Euler method. The system seems to be stiff (due to significant
       difference between pressure and velocity (and volume fraction) values. Hence,
       small spatial step is recommended.
    """

    begin = argparse.ArgumentParser(description = 'This program simulates steady \
                                    influx using drift-flux model')
    begin.add_argument('-alpha', '--initial_gas_fraction', type = float, required = True,
                       help = 'specify initial gas influx concentration (start with 0.01)')
    list_of_args = begin.parse_args(sys.argv[1:])
    α_G0 = list_of_args.initial_gas_fraction

    with resources.open_text('stin', 'input.yaml') as f:
        inputs = yaml.safe_load(f)

    # Two-phase flow occurs at the same very coordinate at which single-phase flow ends.

    # Necessary parameters:
    v_L0 = inputs["v_L0"]
    p_0 = inputs["p_0"]
    L = inputs["L"]
    H = inputs["H"]
    h = inputs["h"]

    # Initialize lists for all the unknowns and coordinate
    x = [0, L]
    α_L_x = [0]
    α_G_x = [0]
    v_L_x = [v_L0]
    v_G_x = [0]
    ρ_G_x = [0]
    p_x = [p_0]

    # Single-phase flow model solution (anlytical):

    # First, assign values to all the variables at the two-phase flow edge (at x=L).
    v_L_x.append(single_v_L(v_L0, L))
    p_x.append(single_p(v_L_x[1], L, p_x[0]))

    # Two-phase flow model solution (numerical):

    kick = BC(α_G0, v_L_x[1], p_x[1])

    # First, assign values to all the variables at the two-phase flow edge (at x=L).
    α_L_x.append(kick.α_L)
    α_G_x.append(kick.α_G)
    v_G_x.append(kick.v_G)
    ρ_G_x.append(kick.ρ_G)

    #Second, realize numercal scheme.
    N = int( (H - L) / h) # amount of spatial steps
    for i in range(1, N+1):
        new_x = x[i] + h
        dp = derivative_p(α_L_x[i], α_G_x[i], ρ_G_x[i], v_L_x[i], v_G_x[i])
        new_p = p_x[i] + h*dp
        new_ρ_G = ρ_G(new_p)
        dv_G = derivative_v_G(v_G_x[i], α_G_x[i], ρ_G_x[i], dp)
        new_v_G = v_G_x[i] + h*dv_G
        dα_G = derivative_α_G(α_G_x[i], ρ_G_x[i], dp, v_G_x[i], dv_G)
        new_α_G = α_G_x[i] + h*dα_G
        new_α_L = α_L(new_α_G)
        dv_L = derivative_v_L(v_L_x[i], α_L_x[i], dα_G)
        new_v_L = v_L_x[i] + h*dv_L
        if new_α_G < cond(new_v_G):
            x.append(new_x)
            p_x.append(new_p) # (1)
            ρ_G_x.append(new_ρ_G) # (2)
            v_G_x.append(new_v_G) # (3)
            α_G_x.append(new_α_G) # (4)
            α_L_x.append(new_α_L) # (5)
            v_L_x.append(new_v_L) # (6)
        else:
            break

    p_x.append(5)
    ρ_G_x.append(4)
    v_G_x.append(3)
    α_G_x.append(1)
    α_L_x.append(0)
    v_L_x.append(2)

    results = [x, α_L_x, α_G_x, v_L_x, v_G_x, ρ_G_x, p_x]
    
    return(results)

raw_results = run()
x = raw_results[0]
results = raw_results[1:]
description = [['α_L', 'liquid fraction', 'liquid fraction (α_L), nondimensional'],\
              ['α_G', 'gas fraction', 'gas fraction (α_G), nondimensional'],\
              ['v_L', 'liquid velocity', 'liquid velocity (v_L), m/s'],\
              ['v_G', 'gas velocity', 'gas velocity (v_G), m/s'],\
              ['ρ_G', 'gas density', 'gas denstiy (ρ_G), kg/m^3'],\
              ['p', 'pressure', 'pressure (p), Pa']]
def plotting(array):
    i = array[len(array)-1]
    plt.figure(description[i][0])
    plt.plot(x, results[i][:(len(results[i])-1)], label=description[i][1])
    plt.xlim( left=100, right=max(x) )
    plt.legend()
    plt.xlabel('wellbore length (x), m')
    plt.ylabel(description[i][2])
    plt.show()
