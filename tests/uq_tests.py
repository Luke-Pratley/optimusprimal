import optimusprimal.map_uncertainty as map_uncertainty
import pytest
import numpy as np

def test_bisection():
    obj = lambda x: np.sum(x**2) - 9
    val = map_uncertainty.bisection_method_credible_interval(obj, [0, 10.] , 1e3, 1e-3)
    assert np.allclose(val, 3., 1e-2)

    obj = lambda x: np.sum(x**2) - 9
    val = map_uncertainty.bisection_method_credible_interval(obj, [-10., 0] , 1e3, 1e-3)
    assert np.allclose(val, -3., 1e-2)

    x_sol = np.zeros((128, 128))
    region_size = 16
    obj = lambda x:  np.sum(np.abs(x)**2)
    bound = 4.
    iters = 1e5
    tol = 1e-12
    error_p, error_m, mean = map_uncertainty.create_credible_region(x_sol, region_size, obj, bound, iters, tol, 5)
    assert np.allclose(error_p.shape, (128/region_size, 128/region_size), 1e-3)
    assert np.allclose(error_m.shape, (128/region_size, 128/region_size), 1e-3)
    assert np.allclose(error_p, 2./region_size, 1e-3)
    assert np.allclose(error_m, -2./region_size, 1e-3)
    assert np.allclose(mean, 0., 1e-12)
    x_sol = np.zeros((128, ))
    region_size = 16
    obj = lambda x:  np.sum(np.abs(x)**2)
    bound =  4
    iters = 1e5
    tol = 1e-12
    error_p, error_m, mean = map_uncertainty.create_credible_region(x_sol, region_size, obj, bound, iters, tol, 5)
    assert np.allclose(error_p.shape, (128/region_size, ), 1e-3)
    assert np.allclose(error_m.shape, (128/region_size, ), 1e-3)
    assert np.allclose(error_p, 2./np.sqrt(region_size), 1e-3)
    assert np.allclose(error_m, -2./np.sqrt(region_size), 1e-3)
