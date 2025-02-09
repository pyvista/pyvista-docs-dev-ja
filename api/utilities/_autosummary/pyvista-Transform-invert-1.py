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
# Check if the transformation is inverted.
#
transform.is_inverted
# Expected:
## False
#
# Invert the transformation and show the matrix.
#
_ = transform.invert()
transform.matrix
# Expected:
## array([[0.5, 0. , 0. , 0. ],
##        [0. , 0.5, 0. , 0. ],
##        [0. , 0. , 0.5, 0. ],
##        [0. , 0. , 0. , 1. ]])
#
# Check that the transformation is inverted.
#
transform.is_inverted
# Expected:
## True
#
# Invert it again to restore it back to its original state.
#
_ = transform.invert()
transform.matrix
# Expected:
## array([[2., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 2., 0.],
##        [0., 0., 0., 1.]])
transform.is_inverted
# Expected:
## False
