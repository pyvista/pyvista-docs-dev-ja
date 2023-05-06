# Create and plot a single polyline.
#
from pyvista import examples
grid = examples.cells.PolyLine()
examples.plot_cell(grid)
#
# List the grid's cells. This could be any number of points.
#
grid.cells
# Expected:
## array([4, 0, 1, 2, 3])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [0.5, 0. , 0. ],
##                  [0.5, 1. , 0. ],
##                  [0. , 1. , 0. ]])
#
grid.celltypes  # same as pyvista.CellType.POLY_LINE
# Expected:
## array([4], dtype=uint8)
