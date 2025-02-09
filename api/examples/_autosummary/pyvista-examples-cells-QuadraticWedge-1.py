# Create and plot a single quadratic wedge.
#
from pyvista import examples
grid = examples.cells.QuadraticWedge()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([15,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
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
##                  [0. , 0.5, 1. ],
##                  [0. , 0. , 0.5],
##                  [1. , 0. , 0.5],
##                  [0. , 1. , 0.5]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_WEDGE
# Expected:
## array([26], dtype=uint8)
