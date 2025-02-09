# Create and plot a single polyhedron.
#
from pyvista import examples
grid = examples.cells.Polyhedron()
examples.plot_cell(grid)
#
# A polyhedron is defined by it's faces. List the grid's faces.
#
grid.get_cell(0).faces  # doctest: +ELLIPSIS
# Expected:
## [Cell...
## ..., Cell...
## ..., Cell...
## ...]
#
grid.celltypes  # same as pyvista.CellType.POLYHEDRON
# Expected:
## array([42], dtype=uint8)
