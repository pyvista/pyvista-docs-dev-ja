# Compose a translation matrix.
#
import pyvista as pv
transform = pv.Transform().translate(1, 2, 3)
transform.matrix
# Expected:
## array([[1., 0., 0., 1.],
##        [0., 1., 0., 2.],
##        [0., 0., 1., 3.],
##        [0., 0., 0., 1.]])
#
# Compose a second translation matrix using ``+``.
#
transform = transform + (1, 1, 1)
transform.matrix
# Expected:
## array([[1., 0., 0., 2.],
##        [0., 1., 0., 3.],
##        [0., 0., 1., 4.],
##        [0., 0., 0., 1.]])
