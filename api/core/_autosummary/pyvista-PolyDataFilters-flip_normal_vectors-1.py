# Flip the normal vectors of a sphere. Show one of the normal vectors
# before and after the flip.
#
import pyvista as pv
sphere = pv.Sphere()
sphere.point_data['Normals'][0]
# Expected:
## pyvista_ndarray([0., 0., 1.], dtype=float32)
#
sphere_flipped = sphere.flip_normal_vectors()
sphere_flipped.point_data['Normals'][0]
# Expected:
## pyvista_ndarray([-0., -0., -1.], dtype=float32)
#
# Note that the sphere's cell ordering has not been affected by this filter.
#
sphere.regular_faces[0]
# Expected:
## array([ 2, 30,  0])
#
sphere_flipped.regular_faces[0]
# Expected:
## array([ 2, 30,  0])
