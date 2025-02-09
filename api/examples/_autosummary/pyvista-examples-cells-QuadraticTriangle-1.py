# Create and plot a single quadratic triangle.
#
from pyvista import examples
grid = examples.cells.QuadraticTriangle()
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
##                  [0. , 1. , 0. ],
##                  [0.5, 0. , 0. ],
##                  [0.5, 0.5, 0. ],
##                  [0. , 0.5, 0. ]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_TRIANGLE
# Expected:
## array([22], dtype=uint8)
