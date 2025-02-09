# Get the face arrays of the five faces of a pyramid.
#
import pyvista as pv
pyramid = pv.Pyramid().extract_surface()
pyramid.irregular_faces
# Expected:
## (array([0, 1, 2, 3]), array([0, 3, 4]), array([0, 4, 1]), array([3, 2, 4]), array([2, 1, 4]))
