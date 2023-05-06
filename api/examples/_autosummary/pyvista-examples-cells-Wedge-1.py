# Create and plot a single wedge.
#
from pyvista import examples
grid = examples.cells.Wedge()
examples.plot_cell(grid)
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
## pyvista_ndarray([[0. , 1. , 0. ],
##                  [0. , 0. , 0. ],
##                  [0. , 0.5, 0.5],
##                  [1. , 1. , 0. ],
##                  [1. , 0. , 0. ],
##                  [1. , 0.5, 0.5]])
#
grid.celltypes  # same as pyvista.CellType.WEDGE
# Expected:
## array([13], dtype=uint8)
