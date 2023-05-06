# Return the x coordinates of a RectilinearGrid.
#
import numpy as np
import pyvista
xrng = np.arange(-10, 10, 10, dtype=float)
yrng = np.arange(-10, 10, 10, dtype=float)
zrng = np.arange(-10, 10, 10, dtype=float)
grid = pyvista.RectilinearGrid(xrng, yrng, zrng)
grid.x
# Expected:
## array([-10.,   0.])
#
# Set the x coordinates of a RectilinearGrid.
#
grid.x = [-10.0, 0.0, 10.0]
grid.x
# Expected:
## array([-10.,   0.,  10.])
