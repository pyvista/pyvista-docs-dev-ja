# Add the 3d affine widget.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
widget = pl.add_affine_transform_widget(actor)
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
