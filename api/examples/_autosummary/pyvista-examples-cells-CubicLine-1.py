# Create and plot a single cubic line.
#
from pyvista import examples
grid = examples.cells.CubicLine()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([4, 0, 1, 2, 3])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[-1.        ,  0.        ,  0.        ],
##                  [ 1.        ,  0.        ,  0.        ],
##                  [-0.33333333,  0.        ,  0.        ],
##                  [ 0.33333333,  0.        ,  0.        ]])
#
grid.celltypes  # same as pyvista.CellType.CUBIC_LINE
# Expected:
## array([35], dtype=uint8)
