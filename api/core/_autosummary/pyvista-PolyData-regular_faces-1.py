# Get the regular face array of a plane with 2x2 arrangement of cells
# as a 4x4 array.
#
import pyvista as pv
plane = pv.Plane(i_resolution=2, j_resolution=2)
plane.regular_faces
# Expected:
## array([[0, 1, 4, 3],
##        [1, 2, 5, 4],
##        [3, 4, 7, 6],
##        [4, 5, 8, 7]])
