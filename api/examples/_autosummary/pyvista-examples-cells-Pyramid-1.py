# Create and plot a single pyramid.
#
from pyvista import examples
grid = examples.cells.Pyramid()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([5, 0, 1, 2, 3, 4])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[ 1.        ,  1.        ,  0.        ],
##                  [-1.        ,  1.        ,  0.        ],
##                  [-1.        , -1.        ,  0.        ],
##                  [ 1.        , -1.        ,  0.        ],
##                  [ 0.        ,  0.        ,  1.60803807]])
#
grid.celltypes  # same as pyvista.CellType.PYRAMID
# Expected:
## array([14], dtype=uint8)
