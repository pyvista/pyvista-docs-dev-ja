# Create and plot a single biquadratic triangle.
#
from pyvista import examples
grid = examples.cells.BiQuadraticTriangle()
examples.plot_cell(grid, cpos='xy')
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([7, 0, 1, 2, 3, 4, 5, 6])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0.        , 0.        , 0.        ],
##                  [1.        , 0.        , 0.        ],
##                  [0.        , 1.        , 0.        ],
##                  [0.5       , 0.        , 0.        ],
##                  [0.5       , 0.5       , 0.        ],
##                  [0.        , 0.5       , 0.        ],
##                  [0.33333333, 0.33333333, 0.        ]])
#
grid.celltypes  # same as pyvista.CellType.BIQUADRATIC_TRIANGLE
# Expected:
## array([34], dtype=uint8)
