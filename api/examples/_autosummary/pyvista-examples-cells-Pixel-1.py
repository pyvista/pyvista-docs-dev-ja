# Create and plot a single pixel.
#
from pyvista import examples
grid = examples.cells.Pixel()
examples.plot_cell(grid, cpos='xy')
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([4, 0, 1, 2, 3])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0., 0., 0.],
##                  [1., 0., 0.],
##                  [0., 1., 0.],
##                  [1., 1., 0.]])
#
grid.celltypes  # same as pyvista.CellType.PIXEL
# Expected:
## array([8], dtype=uint8)
