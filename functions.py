from parameters import γ, C_0, v_s, a

def α_L(α_G):
    α_L = 1 - α_G
    return(α_L)

def ρ_G(p):
    ρ_G = γ * p / a ** 2
    return(ρ_G)

def v_L(v_G, α_G, α_L):
    v_L = v_G * (1 - C_0 * α_G) / (C_0 * α_L) - v_s / (C_0 * α_L)
    return(v_L)
