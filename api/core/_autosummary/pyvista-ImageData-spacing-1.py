# Create a 5 x 5 x 5 uniform grid.
#
import pyvista
grid = pyvista.ImageData(dimensions=(5, 5, 5))
grid.spacing
# Expected:
## (1.0, 1.0, 1.0)
grid.plot(show_edges=True)
#
# Modify the spacing to ``(1, 2, 3)``
#
grid.spacing = (1, 2, 3)
grid.plot(show_edges=True)
