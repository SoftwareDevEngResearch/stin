from parameters import γ, C_0, v_s, a, ρ_L, g, f, D

# Functions for single-phase flow:

def single_v_L(v_L0, L):
    """
       Calculates velocity of a single-phase flow at the given position L along
       the wellbore. See the first equation of the system.

       Args:
           v_L0 (float) - boundary condition for velocity. Can assume any positive
                          value.

       Returns:
           float: the return value (flow velocity). Can assume any positive value;
                  normaly should be equal to the function's argument.
    """
    v_L = v_L0
    return(v_L)

def single_p(v_L, L, p_0):
    """
       Calculates pressure at the given point in a single-phase flow. See the second
       equation of the system.

       Args:
           v_L (float) - flow velocity. Can assume any positive value. It is a
                         variable, not a function.
           L (integer) - point at which pressure is to be calculated. Can assume
                         any positive value.
           p_0 (float) - boundary condition for pressure. Can assume any positive
                         value.

       Returns:
           float: the return value (pressure at the specified point). Can assume
                  any positive value.
    """
    p = -ρ_L * (g + (2*f/D) * v_L**2) * L + p_0
    return(p)

# Functions for two-phase flow:

def derivative_p(α_L, α_G, ρ_G, v_L, v_G): # (1)
    """
       Calculates pressure spatial derivative to be pluged into the expression for
       pressure at the next spatial step (see first equation of the model). It
       returns the value of pressure spatial derivative at the current time step
       and, hence, takes as arguments volume fractions, velocities, and gas density
       at the current spatial step.

       Args:
           α_L (float) - liquid phase volume fraction. Can assume any value
                         from 0 to 1.
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.
           ρ_G (float) - gaseous phase density. Can assume any positive value.
           v_L (float) - liquid phase velocity. Can assume either positive or
                         negative values.
           v_G (float) - gaseous phase velocity. Can assume any positive value.

       Returns:
           float: the return value (pressure derivative at the current spatial
                  step). Can assume any value from negative infinity to 0.
    """
    derivative_p = (-1)*(ρ_L*α_L + ρ_G*α_G) \
                   * ( g + (2*f/D) * (α_L*v_L + α_G*v_G)**2 ) # line continuation operator
    return(derivative_p)

def ρ_G(p): # (2)
    """
       Calculates gas phase density at the next spatial step based on the pressure
       value at the next spatial step (see second equation of the model).

       Args:
           p (float) - flow pressure. Can assume any positive value.

       Returns:
           float: the return value (gaseous phase density). Can assume any
                  positive value.

       Example:
           ρ_G(50000000Pa) = 260kg/m^3
    """
    ρ_G = γ*p / a**2
    return(ρ_G)

def derivative_v_G(v_G, α_G, ρ_G, derivative_p): # (3)
    """
       Calculates gaseous phase spatial velocity derivative at the current spatial
       step, therefore all the arguments assume their values at the current spatial
       step. Is used in the third equation of the system.

       Args:
           v_G (float) - gaseous phase velocity. Can assume any positive value.
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.
           ρ_G (float) - gaseous phase density. Can assume any positive value.
           derivative_p (float) - spatial pressure derivative. Can assume any value
                                  from negative infinity to 0. It is a variable,
                                  not a function.

       Returns:
           float: the return value (gaseous phase velocity). Can assume any
                  positive value.
    """
    derivative_v_G = (-1)*(γ/a**2) * (v_G*α_G*C_0/ρ_G) * derivative_p
    return(derivative_v_G)

def derivative_α_G(α_G, ρ_G, derivative_p, v_G, derivative_v_G): # (4)
    """
       Calculates spatial derivative of gaseous volume fraction at the current
       spatial step. Hence, all the arguments it takes assume their values at
       the current spatial step. It is used in the fourth equation of the system.

       Args:
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.
           ρ_G (float) - gaseous phase density. Can assume any positive value.
           derivative_p (float) - spatial pressure derivative. Can assume any value
                                  from negative infinity to 0. It is a variable,
                                  not a function.
           v_G (float) - gaseous phase velocity. Can assume any positive value.
           derivative_v_G (float) - spatial gas velocity derivative. Can assume
                                    any value. It is a variable, not a function.

       Returns:
           float: the return value (gaseous phase velocity). Can assume any value.
    """
    derivative_α_G = (-1)*α_G * (γ*derivative_p/(ρ_G*a**2) + derivative_v_G/v_G)
    return(α_G)

def α_L(α_G): # (5)
    """
       Calculates liquid phase volume fraction at the next spatial step. Hence,
       the argument it takes assumes its value at the next spatial step also.

       Args:
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.

       Returns:
           float: the return value (liquid phase volume fraction). Can assume
                  any value in the range 0 to 1.

       Example:
           α_L(0.3) = 0.7 - both entities are dimensionless
    """
    α_L = 1 - α_G
    return(α_L)

def derivative_v_L(v_L, α_L, derivative_α_G): # (6)
    """
       Calculates spatial derivative of liquid phase velocity at the current
       spatial step. Hence, all the arguments it takes assume their values at the
       current spatial step. It is used in the second version of the sixth
       equation of the system.

       Args:
           v_L (float) - liquid phase velocity. Can assume either positive or
                         negative values.
           α_L (float) - liquid phase volume fraction. Can assume any value
                         from 0 to 1.
           derivative_α_G (float) - spatial gas fraction derivative. Can assume
                                    any value. It is a variable, not a function.

       Returns:
           float: the return value (spatial liquid velocity derivative). Can assume
                  any value.
    """
    derivative_v_L = v_L*derivative_α_G/α_L
    return(derivative_v_L)

# Function for boundary condition

def BC_v_G(α_L, v_L, α_G):
    """
       The only purpose of this function is to make sure that two-phase flow
       boundary condition for v_G is consistent with the mathematical model. I.e.,
       by the moment an influx occurs I know liquid phase velocity as a result
       of the single-phase model solution. Hence, at the boundary of two-phase
       flow I specify v_L and calculate v_G. Hence, I need a function to find v_G.

       Args:
           α_L (float) - liquid phase volume fraction. Can assume any value
                         from 0 to 1.
           v_L (float) - flow velocity. Can assume any positive value. It is a
                         variable, not a function.
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.

       Returns:
           float: the return value (boundary condition for gaseous phase velocity).
                  Can assume any positive value.
    """
    v_G = (C_0*α_L*v_L + v_s) / (1 - C_0*α_G)
    return(v_G)

# Function that verifies the slip relation condition for gas fraction

def cond(v_G):
    """
       Verifies that liquid velocity is positive (based on the condition obtained
       from the sixth equation of the system).

       Args:
           v_G (float) - gaseous phase velocity. Can assume any positive value.

       Returns:
           float: the return value. Can assume any positive value.
    """
    condition = (1 - v_s/v_G) / C_0
    return(condition)
