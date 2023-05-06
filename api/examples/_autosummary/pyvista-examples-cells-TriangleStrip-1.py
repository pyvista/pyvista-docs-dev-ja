# Create and plot a single triangle strip.
#
from pyvista import examples
grid = examples.cells.TriangleStrip()
examples.plot_cell(grid, cpos='xy')
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([8, 0, 1, 2, 3, 4, 5, 6, 7])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[1., 0., 0.],
##                  [0., 0., 0.],
##                  [1., 1., 0.],
##                  [0., 1., 0.],
##                  [1., 2., 0.],
##                  [0., 2., 0.],
##                  [1., 3., 0.],
##                  [0., 3., 0.]])
#
grid.celltypes  # same as pyvista.CellType.TRIANGLE_STRIP
# Expected:
## array([6], dtype=uint8)
