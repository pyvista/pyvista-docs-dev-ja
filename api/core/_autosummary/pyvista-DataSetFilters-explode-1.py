import numpy as np
import pyvista as pv
xrng = np.linspace(0, 1, 3)
yrng = np.linspace(0, 2, 4)
zrng = np.linspace(0, 3, 5)
grid = pv.RectilinearGrid(xrng, yrng, zrng)
exploded = grid.explode()
exploded.plot(show_edges=True)
