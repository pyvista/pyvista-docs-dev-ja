# Compose a reflection matrix.
#
import pyvista as pv
transform = pv.Transform()
_ = transform.reflect(0, 0, 1)
transform.matrix
# Expected:
## array([[ 1.,  0.,  0.,  0.],
##        [ 0.,  1.,  0.,  0.],
##        [ 0.,  0., -1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second reflection matrix.
#
_ = transform.reflect((1, 0, 0))
transform.matrix
# Expected:
## array([[-1.,  0.,  0.,  0.],
##        [ 0.,  1.,  0.,  0.],
##        [ 0.,  0., -1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
