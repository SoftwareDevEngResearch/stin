from functions import α_L, ρ_G, v_L

# tests for α_L function:

def test_α_L_internal():
    assert α_L(0.3) == 0.7
test_α_L_internal()

def test_α_L_edge_left():
    assert α_L(0) == 1
test_α_L_edge_left()

def test_α_L_edge_right():
    assert α_L(1) == 0
test_α_L_edge_right()

# tests for ρ_G function:

def test_ρ_G_internal():
    assert ρ_G(50000000) == 260
test_ρ_G_internal()

def test_ρ_G_edge_left():
    assert ρ_G(0) == 0
test_ρ_G_edge_left()

# tests for v_L functions

def test_v_L_internal():
    assert v_L(0.9, 0.4, 0.6) <= -0.44
test_v_L_internal()

def test_v_L_edge():
    assert v_L(0, 0, 1) <= -0.72
test_v_L_edge()
