# Create an actor and show its initial orientation.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor.orientation
# Expected:
## (0.0, -0.0, 0.0)
#
# Set the orientation using a 3x3 matrix.
#
actor.rotation_from([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
actor.orientation
# Expected:
## (0.0, -180.0, -89.99999999999999)
