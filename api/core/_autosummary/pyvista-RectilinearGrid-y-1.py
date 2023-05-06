# Return the y coordinates of a RectilinearGrid.
#
import numpy as np
import pyvista
xrng = np.arange(-10, 10, 10, dtype=float)
yrng = np.arange(-10, 10, 10, dtype=float)
zrng = np.arange(-10, 10, 10, dtype=float)
grid = pyvista.RectilinearGrid(xrng, yrng, zrng)
grid.y
# Expected:
## array([-10.,   0.])
#
# Set the y coordinates of a RectilinearGrid.
#
grid.y = [-10.0, 0.0, 10.0]
grid.y
# Expected:
## array([-10.,   0.,  10.])
