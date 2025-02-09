# Flip the faces of a sphere. Show the point ids of the first cell
# before and after the flip.
#
import pyvista as pv
sphere = pv.Sphere()
sphere.regular_faces[0]
# Expected:
## array([ 2, 30,  0])
#
sphere_flipped = sphere.flip_faces()
sphere_flipped.regular_faces[0]
# Expected:
## array([ 0, 30,  2])
#
# Note that the sphere also has pre-computed normals which have not been
# affected by this filter.
#
sphere.point_data['Normals'][0]
# Expected:
## pyvista_ndarray([0., 0., 1.], dtype=float32)
#
sphere_flipped.point_data['Normals'][0]
# Expected:
## pyvista_ndarray([0., 0., 1.], dtype=float32)
