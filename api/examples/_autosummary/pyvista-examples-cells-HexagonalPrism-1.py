# Create and plot a single hexagonal prism.
#
from pyvista import examples
grid = examples.cells.HexagonalPrism()
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
## pyvista_ndarray([[ 0. ,  0. ,  1. ],
##                  [ 1. ,  0. ,  1. ],
##                  [ 1.5,  0.5,  1. ],
##                  [ 1. ,  1. ,  1. ],
##                  [ 0. ,  1. ,  1. ],
##                  [-0.5,  0.5,  1. ],
##                  [ 0. ,  0. ,  0. ],
##                  [ 1. ,  0. ,  0. ],
##                  [ 1.5,  0.5,  0. ],
##                  [ 1. ,  1. ,  0. ],
##                  [ 0. ,  1. ,  0. ],
##                  [-0.5,  0.5,  0. ]])
#
grid.celltypes  # same as pyvista.CellType.HEXAGONAL_PRISM
# Expected:
## array([16], dtype=uint8)
