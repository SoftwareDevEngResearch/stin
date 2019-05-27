from .functions import α_L, ρ_G, BC_v_G

class BC:
    """
       Boundary conditions for two-phase flow. Boundary conditions can't be
       assigned randomly because they are connected by the equations from the
       system. Thus, boundary conditions for v_L and p are calculated from the
       sinle-phase flow solution, for α_G - specified by user randomly. The other
       boundary conditions are to be calculated from the equations. This class
       is devoted for it.
       
       Attributes:
             α_L : liquid phase volume fraction, dimensionless
             α_G : gaseous phase volume fraction, dimensionless
             v_L : liquid phase velocity, [m/s]
             v_G : gaseous phase velocity, [m/s]
             ρ_G : gaseous phase density, [kg/m^3]
             p : flow pressure, [Pa]
    """
    def __init__(self, α_G, v_L, p):
       """
          Initializes the flow's boundary conditions with supplied values for
          gaseous phase volume fraction, gaseous phase velocity and flow pressure.
       """
       self.α_L = α_L(α_G)
       self.α_G = α_G
       self.v_G = BC_v_G(α_L(α_G), v_L, α_G)
       self.ρ_G = ρ_G(p)
