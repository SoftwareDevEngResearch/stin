from parameters import γ, C_0, v_s, a

def α_L(α_G):
    """
       This function calculates liquid phase
       volume fraction based on the gas phase volume fraction.
       I deliberately specify gas fraction and then calculate
       liquid fraction because gas fraction is what I am focusing on.
    """
    α_L = 1 - α_G # first closure relation
    return(α_L)

def ρ_G(p):
    """
       This function calculates gas phase density based on the 
       downhole pressure which I specify. I am more interested in 
       ability to play with pressure. That's why I specify namely 
       pressure and then calculate gas density.
    """
    ρ_G = γ * p / a ** 2 # second closure relation
    return(ρ_G)

def v_L(v_G, α_G, α_L):
    """
       This function caculates liquid phase velocity
       based on the gas phase velocity which I specify manualy.
       It doesn't matter much which velocity I want to vary.
       I randomly chose to specify manualuy gas velocity and then
       calculate liquid velocity.
    """
    v_L = v_G * (1 - C_0 * α_G) / (C_0 * α_L) - v_s / (C_0 * α_L) # third closure relation
    return(v_L)
