# Create and plot a single hexahedron.
#
from pyvista import examples
grid = examples.cells.Hexahedron()
examples.plot_cell(grid)
