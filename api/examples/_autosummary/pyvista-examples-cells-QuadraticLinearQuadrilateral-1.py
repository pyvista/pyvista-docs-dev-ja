# Create and plot a single quadratic linear quadrilateral.
#
from pyvista import examples
grid = examples.cells.QuadraticLinearQuadrilateral()
examples.plot_cell(grid, cpos='xy')
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
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [1. , 0. , 0. ],
##                  [1. , 1. , 0. ],
##                  [0. , 1. , 0. ],
##                  [0.5, 0. , 0. ],
##                  [0.5, 1. , 0. ]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_LINEAR_QUAD
# Expected:
## array([30], dtype=uint8)
