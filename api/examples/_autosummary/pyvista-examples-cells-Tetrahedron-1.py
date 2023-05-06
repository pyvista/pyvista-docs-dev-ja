# Create and plot a single tetrahedron.
#
from pyvista import examples
grid = examples.cells.Tetrahedron()
examples.plot_cell(grid)
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
## pyvista_ndarray([[ 1.,  1.,  1.],
##                  [ 1., -1., -1.],
##                  [-1.,  1., -1.],
##                  [-1., -1.,  1.]])
#
grid.celltypes  # same as pyvista.CellType.TETRA
# Expected:
## array([10], dtype=uint8)
