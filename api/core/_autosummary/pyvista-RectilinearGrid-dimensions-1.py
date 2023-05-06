# Create a uniform grid with dimensions ``(1, 2, 3)``.
#
import pyvista
grid = pyvista.UniformGrid(dimensions=(2, 3, 4))
grid.dimensions
# Expected:
## (2, 3, 4)
grid.plot(show_edges=True)
#
# Set the dimensions to ``(3, 4, 5)``
#
grid.dimensions = (3, 4, 5)
grid.plot(show_edges=True)
