# Compose an arbitrary transformation.
#
import pyvista as pv
transform = pv.Transform().scale(2.0)
transform.matrix
# Expected:
## array([[2., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 2., 0.],
##        [0., 0., 0., 1.]])
#
# Reset the transformation to the identity matrix.
#
_ = transform.identity()
transform.matrix
# Expected:
## array([[1., 0., 0., 0.],
##        [0., 1., 0., 0.],
##        [0., 0., 1., 0.],
##        [0., 0., 0., 1.]])
