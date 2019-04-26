from parameters import γ, C_0, v_s, a

def α_L(α_G):
    """
       This function calculates liquid phase  volume fraction based on the gas
       phase volume fraction. I deliberately specify gas fraction and then calculate
       liquid fraction because gas fraction is what I am focusing on.

       Args:
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.

       Retruns:
           float: the return value (liquid phase volume fraction). Can assume
                  any value in the range 0 to 1.

       Example:
           α_L(0.3) = 0.7
    """
    α_L = 1 - α_G # first closure relation
    return(α_L)

def ρ_G(p):
    """
       This function calculates gas phase density based on the downhole pressure
       which I specify. I am more interested in  ability to play with pressure.
       That's why I specify namely pressure and then calculate gas density.

       Args:
           p (float) - flow pressure. Can assume any positive value.

       Retruns:
           float: the return value (gaseous phase density). Can assume any
                  positive value.

       Example:
           ρ_G(50000000) = 260
    """
    ρ_G = γ * p / a ** 2 # second closure relation
    return(ρ_G)

def v_L(v_G, α_G, α_L):
    """
       This function caculates liquid phase velocity based on the gas phase
       velocity which I specify manualy. It doesn't matter much which velocity I
       want to vary. I randomly chose to specify manualuy gas velocity and then
       calculate liquid velocity.

       Args:
           v_G (float) - gaseous phase velocity. Can assume any positive value.
           α_G (float) - gaseous phase volume fraction. Can assume any value
                         from 0 to 1.
           α_L (float) - liquid phase volume fraction. Can assume any value
                         from 0 to 1.

       Retruns:
           float: the return value (liquid phase velocity). Can assume any
                  positive or negative value.

       Example:
           v_L(0.9, 0.4, 0.6) = -0.44
    """
    v_L = v_G * (1 - C_0 * α_G) / (C_0 * α_L) - v_s / (C_0 * α_L) # third closure relation
    return(v_L)
