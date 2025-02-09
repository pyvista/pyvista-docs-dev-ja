# Create and plot a single biquadratic quadrilateral.
#
from pyvista import examples
grid = examples.cells.BiQuadraticQuadrilateral()
examples.plot_cell(grid, cpos='xy')
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([9, 0, 1, 2, 3, 4, 5, 6, 7, 8])
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
##                  [0. , 0.5, 0. ],
##                  [0.5, 0.5, 0. ]])
#
grid.celltypes  # same as pyvista.CellType.BIQUADRATIC_QUAD
# Expected:
## array([28], dtype=uint8)
