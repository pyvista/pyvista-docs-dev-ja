# Create and plot a single pentagonal prism.
#
from pyvista import examples
grid = examples.cells.PentagonalPrism()
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
## pyvista_ndarray([[1., 0., 0.],
##                  [3., 0., 0.],
##                  [4., 2., 0.],
##                  [2., 4., 0.],
##                  [0., 2., 0.],
##                  [1., 0., 4.],
##                  [3., 0., 4.],
##                  [4., 2., 4.],
##                  [2., 4., 4.],
##                  [0., 2., 4.]])
#
grid.celltypes  # same as pyvista.CellType.PENTAGONAL_PRISM
# Expected:
## array([15], dtype=uint8)
