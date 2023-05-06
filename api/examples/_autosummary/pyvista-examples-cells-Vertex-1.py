# Create and plot a single vertex.
#
from pyvista import examples
grid = examples.cells.Vertex()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([1, 0])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0., 0., 0.]])
#
grid.celltypes  # same as pyvista.CellType.VERTEX
# Expected:
## array([1], dtype=uint8)
