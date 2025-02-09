# Create and plot a single quadratic hexahedron.
#
from pyvista import examples
grid = examples.cells.QuadraticHexahedron()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([20,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
##        16, 17, 18, 19])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [1. , 0. , 0. ],
##                  [1. , 1. , 0. ],
##                  [0. , 1. , 0. ],
##                  [0. , 0. , 1. ],
##                  [1. , 0. , 1. ],
##                  [1. , 1. , 1. ],
##                  [0. , 1. , 1. ],
##                  [0.5, 0. , 0. ],
##                  [1. , 0.5, 0. ],
##                  [0.5, 1. , 0. ],
##                  [0. , 0.5, 0. ],
##                  [0.5, 0. , 1. ],
##                  [1. , 0.5, 1. ],
##                  [0.5, 1. , 1. ],
##                  [0. , 0.5, 1. ],
##                  [0. , 0. , 0.5],
##                  [1. , 0. , 0.5],
##                  [1. , 1. , 0.5],
##                  [0. , 1. , 0.5]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_HEXAHEDRON
# Expected:
## array([25], dtype=uint8)
