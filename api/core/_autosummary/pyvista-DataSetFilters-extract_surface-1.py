# Extract the surface of an UnstructuredGrid.
#
import pyvista
from pyvista import examples
grid = examples.load_hexbeam()
surf = grid.extract_surface()
type(surf)
# Expected:
## <class 'pyvista.core.pointset.PolyData'>
surf["vtkOriginalPointIds"]
# Expected:
## pyvista_ndarray([ 0,  2, 36, 27,  7,  8, 81,  1, 18,  4, 54,  3,  6, 45,
##                  72,  5, 63,  9, 35, 44, 11, 16, 89, 17, 10, 26, 62, 13,
##                  12, 53, 80, 15, 14, 71, 19, 37, 55, 20, 38, 56, 21, 39,
##                  57, 22, 40, 58, 23, 41, 59, 24, 42, 60, 25, 43, 61, 28,
##                  82, 29, 83, 30, 84, 31, 85, 32, 86, 33, 87, 34, 88, 46,
##                  73, 47, 74, 48, 75, 49, 76, 50, 77, 51, 78, 52, 79, 64,
##                  65, 66, 67, 68, 69, 70])
surf["vtkOriginalCellIds"]
# Expected:
## pyvista_ndarray([ 0,  0,  0,  1,  1,  1,  3,  3,  3,  2,  2,  2, 36, 36,
##                  36, 37, 37, 37, 39, 39, 39, 38, 38, 38,  5,  5,  9,  9,
##                  13, 13, 17, 17, 21, 21, 25, 25, 29, 29, 33, 33,  4,  4,
##                   8,  8, 12, 12, 16, 16, 20, 20, 24, 24, 28, 28, 32, 32,
##                   7,  7, 11, 11, 15, 15, 19, 19, 23, 23, 27, 27, 31, 31,
##                  35, 35,  6,  6, 10, 10, 14, 14, 18, 18, 22, 22, 26, 26,
##                  30, 30, 34, 34])
#
# Note that in the "vtkOriginalCellIds" array, the same original cells
# appears multiple times since this array represents the original cell of
# each surface cell extracted.
