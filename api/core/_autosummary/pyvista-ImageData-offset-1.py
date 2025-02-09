# Create a ``ImageData`` and show that the offset is zeros by default.
#
import pyvista as pv
grid = pv.ImageData(dimensions=(10, 10, 10))
grid.offset
# Expected:
## (0, 0, 0)
#
# The offset defines the minimum extent.
grid.extent
# Expected:
## (0, 9, 0, 9, 0, 9)
#
# Set the offset to a new value for all axes.
#
grid.offset = 2
grid.offset
# Expected:
## (2, 2, 2)
#
# Show the extent again. Note how all values have increased by the offset value.
#
grid.extent
# Expected:
## (2, 11, 2, 11, 2, 11)
#
# Set the offset for each axis separately and show the extent again.
#
grid.offset = (-1, -2, -3)
grid.extent
# Expected:
## (-1, 8, -2, 7, -3, 6)
