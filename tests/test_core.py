import numpy as np
from ibmbfire.core import compute_ibmb_curve


def test_compute_ibmb_curve_length():
    # random b
    t, T = compute_ibmb_curve(5,4,2.5,1,1.5,1.5,20,600,500, 300.0)
    assert len(t) == len(T)
    assert len(t) > 0


def test_compute_ibmb_curve_values():
    # check T0
    t, T = compute_ibmb_curve(1,1,1,1,1,1,15,100,100, 200.0)
    assert np.isclose(T[0], 15)
