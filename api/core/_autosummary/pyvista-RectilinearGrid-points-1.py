import numpy as np
import pyvista as pv
xrng = np.arange(-10, 10, 10, dtype=float)
yrng = np.arange(-10, 10, 10, dtype=float)
zrng = np.arange(-10, 10, 10, dtype=float)
grid = pv.RectilinearGrid(xrng, yrng, zrng)
grid.points
# Expected:
## array([[-10., -10., -10.],
##        [  0., -10., -10.],
##        [-10.,   0., -10.],
##        [  0.,   0., -10.],
##        [-10., -10.,   0.],
##        [  0., -10.,   0.],
##        [-10.,   0.,   0.],
##        [  0.,   0.,   0.]])
