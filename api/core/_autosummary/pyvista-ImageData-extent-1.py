# Create a ``ImageData`` and show its extent.
#
import pyvista
grid = pyvista.ImageData(dimensions=(10, 10, 10))
grid.extent
# Expected:
## (0, 9, 0, 9, 0, 9)
#
grid.extent = (2, 5, 2, 5, 2, 5)
grid.extent
# Expected:
## (2, 5, 2, 5, 2, 5)
#
# Note how this also modifies the grid bounds and dimensions. Since we
# use default spacing of 1 here, the bounds match the extent exactly.
#
grid.bounds
# Expected:
## (2.0, 5.0, 2.0, 5.0, 2.0, 5.0)
grid.dimensions
# Expected:
## (4, 4, 4)
