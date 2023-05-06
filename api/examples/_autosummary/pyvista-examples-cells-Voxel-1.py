# Create and plot a single voxel.
#
from pyvista import examples
grid = examples.cells.Voxel()
examples.plot_cell(grid)
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
## pyvista_ndarray([[0., 0., 0.],
##                  [1., 0., 0.],
##                  [1., 1., 0.],
##                  [0., 1., 0.],
##                  [0., 0., 1.],
##                  [1., 0., 1.],
##                  [1., 1., 1.],
##                  [0., 1., 1.]])
#
grid.celltypes  # same as pyvista.CellType.VOXEL
# Expected:
## array([11], dtype=uint8)
