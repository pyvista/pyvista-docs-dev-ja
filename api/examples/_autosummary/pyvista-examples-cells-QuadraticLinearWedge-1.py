# Create and plot a single quadratic linear wedge.
#
from pyvista import examples
grid = examples.cells.QuadraticLinearWedge()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([12,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [1. , 0. , 0. ],
##                  [0. , 1. , 0. ],
##                  [0. , 0. , 1. ],
##                  [1. , 0. , 1. ],
##                  [0. , 1. , 1. ],
##                  [0.5, 0. , 0. ],
##                  [0.5, 0.5, 0. ],
##                  [0. , 0.5, 0. ],
##                  [0.5, 0. , 1. ],
##                  [0.5, 0.5, 1. ],
##                  [0. , 0.5, 1. ]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_LINEAR_WEDGE
# Expected:
## array([31], dtype=uint8)
