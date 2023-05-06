# Create and plot a single poly vertex.
#
from pyvista import examples
grid = examples.cells.PolyVertex()
examples.plot_cell(grid)
#
# List the grid's cells. This could be any number of points.
#
grid.cells
# Expected:
## array([6, 0, 1, 2, 3, 4, 5])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [1. , 0. , 0. ],
##                  [0. , 1. , 0. ],
##                  [0. , 0. , 1. ],
##                  [1. , 0. , 0.4],
##                  [0. , 1. , 0.6]])
#
grid.celltypes  # same as pyvista.CellType.POLY_VERTEX
# Expected:
## array([2], dtype=uint8)
