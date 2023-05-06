# Create and plot a single polygon.
#
from pyvista import examples
grid = examples.cells.Polygon()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([6, 0, 1, 2, 3, 4, 5])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[ 0. ,  0. ,  0. ],
##                  [ 1. , -0.1,  0. ],
##                  [ 0.8,  0.5,  0. ],
##                  [ 1. ,  1. ,  0. ],
##                  [ 0.6,  1.2,  0. ],
##                  [ 0. ,  0.8,  0. ]])
#
grid.celltypes  # same as pyvista.CellType.POLYGON
# Expected:
## array([7], dtype=uint8)
