# Create and plot a single biquadratic quadratic hexahedron.
#
from pyvista import examples
grid = examples.cells.BiQuadraticQuadraticHexahedron()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([24,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
##        16, 17, 18, 19, 20, 21, 22, 23])
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
##                  [0. , 1. , 0.5],
##                  [0. , 0.5, 0.5],
##                  [1. , 0.5, 0.5],
##                  [0.5, 0. , 0.5],
##                  [0.5, 1. , 0.5]])
#
grid.celltypes  # same as pyvista.CellType.BIQUADRATIC_QUADRATIC_HEXAHEDRON
# Expected:
## array([33], dtype=uint8)
