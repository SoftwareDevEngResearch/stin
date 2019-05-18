from ..code.functions import single_v_L, single_p, derivative_p, α_L, ρ_G, \
                             BC_v_G, derivative_v_G, derivative_α_G, \
                             derivative_v_L, cond

# tests for single_v_l function:
def test_single_v_L_internal():
    assert single_v_L(0.8, 150) == 0.8

# tests for single_p function:
def test_single_p_internal():
    assert single_p(1, 200, 10000000) <= 11000000
def test_single_p_edge():
    assert single_p(0.8, 0, 10000000) == 10000000

# tests for derivative_p function:
def test_derivative_p_edge_left():
    assert derivative_p(0.1, 0.9, 10, 0.5, 0.6) < 0
def test_derivative_p_internal():
    assert derivative_p(0.5, 0.5, 10, 0.5, 0.6) < 0
def test_derivative_p_edge_right():
    assert derivative_p(0.9, 0.1, 10, 0.5, 0.6) < 0

# tests for ρ_G function:
def test_ρ_G_internal():
    assert ρ_G(50000000) == 260
def test_ρ_G_edge_left():
    assert ρ_G(0) == 0

# tests for derivative_v_G function:
def test_derivative_v_G_edge_left():
    assert derivative_v_G(0.1, 0.9, 10, -2) > 0
def test_derivative_v_G_internal():
    assert derivative_v_G(0.5, 0.5, 10, -2) > 0
def test_derivative_v_G_edge_right():
    assert derivative_v_G(0.8, 0.1, 10, -2) > 0

# tests for derivative_α_G function:
def test_derivative_α_G_edge_left():
    assert derivative_α_G(0.2, 10, -2, 0.8, 1) > 0
def test_derivative_α_G_edge_right():
    assert derivative_α_G(0.9, 10, 2, 0.8, -1) > 0

# tests for α_L function:
def test_α_L_internal():
    assert α_L(0.3) == 0.7
def test_α_L_edge_left():
    assert α_L(0) == 1
def test_α_L_edge_right():
    assert α_L(1) == 0

# tests for derivative_v_L function:
def test_derivative_v_L_edge_left():
    assert derivative_v_L(0.8, 0.2, -1) < 0
def test_derivative_v_L_internal():
    assert derivative_v_L(0.8, 0.2, 0) == 0
def test_derivative_v_L_edge_right():
    assert derivative_v_L(0.8, 0.2, 1) > 0

# tests for BC_v_G function:
def test_BC_v_G_internal():
    assert BC_v_G(0.8, 0.5, 0.2) >= 0.8

# tests for cond function:
def test_cond_internal():
    assert cond(0.8) > 0.6
