# Compose a reflection about the y-axis.
#
import pyvista as pv
transform = pv.Transform()
_ = transform.flip_y()
transform.matrix
# Expected:
## array([[ 1.,  0.,  0.,  0.],
##        [ 0., -1.,  0.,  0.],
##        [ 0.,  0.,  1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second reflection, but this time about a point.
#
_ = transform.flip_y(point=(4, 5, 6))
transform.matrix
# Expected:
## array([[ 1.,  0.,  0.,  0.],
##        [ 0.,  1.,  0., 10.],
##        [ 0.,  0.,  1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
