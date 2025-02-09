# Create a ``ImageData`` and show its extent.
#
import pyvista as pv
grid = pv.ImageData(dimensions=(10, 10, 10))
grid.extent
# Expected:
## (0, 9, 0, 9, 0, 9)
#
grid.extent = (2, 5, 2, 5, 2, 5)
grid.extent
# Expected:
## (2, 5, 2, 5, 2, 5)
#
# Note how this also modifies the grid's :attr:`offset`, :attr:`dimensions`,
# and :attr:`bounds`. Since we use default spacing of 1 here, the bounds
# match the extent exactly.
#
grid.offset
# Expected:
## (2, 2, 2)
#
grid.dimensions
# Expected:
## (4, 4, 4)
#
grid.bounds
# Expected:
## BoundsTuple(x_min=2.0, x_max=5.0, y_min=2.0, y_max=5.0, z_min=2.0, z_max=5.0)
