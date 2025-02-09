# Create a scaling transform.
#
import pyvista as pv
transform = pv.Transform().scale(1, 2, 3)
transform.matrix
# Expected:
## array([[1., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 3., 0.],
##        [0., 0., 0., 1.]])
#
# Copy the transform.
#
copied = transform.copy()
copied.matrix
# Expected:
## array([[1., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 3., 0.],
##        [0., 0., 0., 1.]])
#
copied is transform
# Expected:
## False
