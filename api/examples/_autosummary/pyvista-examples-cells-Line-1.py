# Create and plot a single line.
#
from pyvista import examples
grid = examples.cells.Line()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([2, 0, 1])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0., 0., 0.],
##                  [1., 0., 0.]])
#
grid.celltypes  # same as pyvista.CellType.LINE
# Expected:
## array([3], dtype=uint8)
