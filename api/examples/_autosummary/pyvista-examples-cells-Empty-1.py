# Create a single empty cell.
#
from pyvista import examples
grid = examples.cells.Empty()
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([0])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([], shape=(0, 3), dtype=float64)
#
grid.celltypes  # same as pyvista.CellType.EMPTY_CELL
# Expected:
## array([0], dtype=uint8)
