# Return the indices of the first two cells from the example hex
# beam.  Note how the cells have "padding" indicating the number
# of points per cell.
#
import pyvista
from pyvista import examples
grid = examples.load_hexbeam()
grid.cells[:18]
# Expected:
## array([ 8,  0,  2,  8,  7, 27, 36, 90, 81,  8,  2,  1,  4,  8, 36, 18, 54,
##        90])
#
# While you cannot change the array inplace, you can overwrite it. For example:
#
grid.cells = [8, 0, 1, 2, 3, 4, 5, 6, 7]
