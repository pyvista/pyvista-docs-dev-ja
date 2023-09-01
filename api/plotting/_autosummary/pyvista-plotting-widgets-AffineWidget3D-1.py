# Create the affine widget outside of the plotter and add it.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
widget = pv.AffineWidget3D(pl, actor)
pl.show()
#
# Access the transform from the actor.
#
actor.user_matrix
# Expected:
## array([[1., 0., 0., 0.],
##        [0., 1., 0., 0.],
##        [0., 0., 1., 0.],
##        [0., 0., 0., 1.]])
