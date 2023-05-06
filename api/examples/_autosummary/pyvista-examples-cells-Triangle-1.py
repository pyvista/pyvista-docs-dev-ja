# Create and plot a single triangle.
#
from pyvista import examples
grid = examples.cells.Triangle()
examples.plot_cell(grid, cpos='xy')
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([3, 0, 1, 2])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[1., 0., 0.],
##                  [0., 0., 0.],
##                  [0., 1., 0.]])
#
grid.celltypes  # same as pyvista.CellType.TRIANGLE
# Expected:
## array([5], dtype=uint8)
