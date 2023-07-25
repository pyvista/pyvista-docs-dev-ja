# Get the face array of a tetrahedron as a 4x3 array
#
import pyvista as pv
tetra = pv.Tetrahedron()
tetra.regular_faces
# Expected:
## array([[0, 1, 2],
##        [1, 3, 2],
##        [0, 2, 3],
##        [0, 3, 1]])
