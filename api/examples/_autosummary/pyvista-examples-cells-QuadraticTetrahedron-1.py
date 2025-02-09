# Create and plot a single quadratic tetrahedron.
#
from pyvista import examples
grid = examples.cells.QuadraticTetrahedron()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([10,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0. , 0. , 0. ],
##                  [1. , 0. , 0. ],
##                  [0. , 1. , 0. ],
##                  [0. , 0. , 1. ],
##                  [0.5, 0. , 0. ],
##                  [0.5, 0.5, 0. ],
##                  [0. , 0.5, 0. ],
##                  [0. , 0. , 0.5],
##                  [0.5, 0. , 0.5],
##                  [0. , 0.5, 0.5]])
#
grid.celltypes  # same as pyvista.CellType.QUADRATIC_TETRA
# Expected:
## array([24], dtype=uint8)
