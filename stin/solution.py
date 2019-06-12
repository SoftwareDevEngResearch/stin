from .functions import single_v_L, single_p, derivative_p, ρ_G, derivative_v_G, \
                       derivative_α_G, α_L, derivative_v_L, cond
from .boundary_conditions import BC
from importlib import resources
import matplotlib.pyplot as plt
import yaml

def run(α_G0):
    """
       At first, the analytical solution for a single-phase flow is used to find pressure
       and velocity of liquid at the point where gas influx occurs.
       At second, system of equation describing gas-liquid flow will be solved numerically
       via explicit Euler method. The system seems to be stiff (due to significant
       difference between pressure and velocity (and volume fraction) values. Hence,
       small spatial step is recommended. This function solves the system of equations
       for the unknowns: *α_L - volume fraction of the liquid phase*, *α_G - volume
       fraction of the gaseous phase*, *v_L - velocity of the liquid phase*,
       *v_G - velocity of the gaseous phase*, *ρ_G - density of the gaseous phase*,
       *p - pressure of the mixture (i.e., of the gas-liquid flow)*.

       Args:
           α_G_0 (float) - boundary condition for gaseous phase volume fraction.
                           Can assume any value from 0 to 1 (not including the
                           margins).

       Returns:
           python list of lists of lists: the return iterable. Each item in the
                                          iterable contains spatial variable and
                                          one of the unknowns. It is done in order
                                          to simplify dealing with plotting function.
    """

    # For the releases 0.1.0 and 0.2.0, user is only allowed use gaseous phase
    # volume fraction as an input parameter. Other input parameters are plased
    # into the input file input.yaml and their change can entail simulation failure.

    with resources.open_text('stin', 'input.yaml') as f:
        inputs = yaml.safe_load(f)

    # α_G0 is the first input parameter. Other input parameters are:
    v_L0 = inputs["v_L0"]
    p_0 = inputs["p_0"]
    L = inputs["L"]
    H = inputs["H"]
    h = inputs["h"]

    # Initialize lists for all the unknowns and coordinate. These lists will be
    # the function's return.
    x = [0, L]
    α_L_x = [0]
    α_G_x = [0]
    v_L_x = [v_L0]
    v_G_x = [0]
    ρ_G_x = [0]
    p_x = [p_0]

    # Single-phase flow model solution (anlytical):

    # Two-phase flow occurs at the same very coordinate at which single-phase flow ends.
    # Having analytical solution for single-phase flow, velocity and pressure of
    # single-phase flow at x = L (coordinate where two-phase flow begins) can be
    # used as boundary conditions for the two-phase flow.
    v_L_x.append(single_v_L(v_L0, L))
    p_x.append(single_p(v_L_x[1], L, p_x[0]))

    # Two-phase flow model solution (numerical):

    kick = BC(α_G0, v_L_x[1], p_x[1])

    # First, assign values to all the variables at the two-phase flow edge (at x=L),
    # i.e., created boundary conditions for two-phase flow.
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
        # The following if block is necessary for capturing the condition imposed
        # by the 6th equation of the system (prevents v_L from going negative).
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
    # The markers are added to each of the unknowns in order to realize plotting
    # as one function.
    p_x.append(5)
    ρ_G_x.append(4)
    v_G_x.append(3)
    α_G_x.append(1)
    α_L_x.append(0)
    v_L_x.append(2)

    results = [ [x, α_L_x], [x, α_G_x], [x, v_L_x], [x, v_G_x], [x, ρ_G_x], [x, p_x] ]

    return(results)

# Plotting flow parameters against spatial coordinate is the ultimate goal of
# this package.
def plotting(array):
    """
       Plots the results against spatial coordinate. Every unknown being a list,
       has a marker as the last member of the list. This function recognizes which
       unknown is taken as an argument by its marker.

       Args:
           array (list of lists) - first item in the list is a list of values of
                                   spatial coordinate; second item is a list of
                                   values of one of the unknowns.

       Returns:
           plot: the return value (matplotlib figures). Shows an unknonw vs x.
    """
    x = array[0]
    results = array[1]
    description = [['α_L', 'liquid fraction', 'liquid fraction (α_L), nondimensional'],\
                  ['α_G', 'gas fraction', 'gas fraction (α_G), nondimensional'],\
                  ['v_L', 'liquid velocity', 'liquid velocity (v_L), m/s'],\
                  ['v_G', 'gas velocity', 'gas velocity (v_G), m/s'],\
                  ['ρ_G', 'gas density', 'gas denstiy (ρ_G), kg/m^3'],\
                  ['p', 'pressure', 'pressure (p), Pa']]
    i = results[len(results)-1] # looks for the marker of the given array
    plt.figure(description[i][0])
    plt.plot(x, results[:(len(results)-1)], label=description[i][1])
    plt.xlim( left=100, right=max(x) )
    plt.legend()
    plt.xlabel('wellbore length (x), m')
    plt.ylabel(description[i][2])
    plt.show()
