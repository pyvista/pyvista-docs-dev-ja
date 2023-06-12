# Divide a rectangular grid into tetrahedrons. Each cell contains by
# default 5 tetrahedrons.
#
# First, create and plot the grid.
#
import numpy as np
import pyvista as pv
xrng = np.linspace(0, 1, 2)
yrng = np.linspace(0, 1, 2)
zrng = np.linspace(0, 2, 3)
grid = pv.RectilinearGrid(xrng, yrng, zrng)
grid.plot()
#
# Now, generate the tetrahedra plot in the exploded view of the cell.
#
tet_grid = grid.to_tetrahedra()
tet_grid.explode(factor=0.5).plot(show_edges=True)
#
# Take the same grid but divide the first cell into 5 cells and the other
# cell into 12 tetrahedrons per cell.
#
tet_grid = grid.to_tetrahedra(mixed=[5, 12])
tet_grid.explode(factor=0.5).plot(show_edges=True)
