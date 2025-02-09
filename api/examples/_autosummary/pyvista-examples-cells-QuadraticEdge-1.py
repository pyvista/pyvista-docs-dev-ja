# Create and plot a single quadratic edge.
#
from pyvista import examples
grid = examples.cells.QuadraticEdge()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([3, 0, 1, 2])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [1. , 0. , 0. ],
##                  [0.5, 0. , 0. ]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_EDGE
# Expected:
## array([21], dtype=uint8)
