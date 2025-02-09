# Create and plot a single quadratic quadrilateral.
#
from pyvista import examples
grid = examples.cells.QuadraticQuadrilateral()
examples.plot_cell(grid, cpos='xy')
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([8, 0, 1, 2, 3, 4, 5, 6, 7])
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
##                  [1. , 0.5, 0. ],
##                  [0.5, 1. , 0. ],
##                  [0. , 0.5, 0. ]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_QUAD
# Expected:
## array([23], dtype=uint8)
