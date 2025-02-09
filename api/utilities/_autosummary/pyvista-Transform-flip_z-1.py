# Compose a reflection about the z-axis.
#
import pyvista as pv
transform = pv.Transform()
_ = transform.flip_z()
transform.matrix
# Expected:
## array([[ 1.,  0.,  0.,  0.],
##        [ 0.,  1.,  0.,  0.],
##        [ 0.,  0., -1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second reflection, but this time about a point.
#
_ = transform.flip_z(point=(4, 5, 6))
transform.matrix
# Expected:
## array([[ 1.,  0.,  0.,  0.],
##        [ 0.,  1.,  0.,  0.],
##        [ 0.,  0.,  1., 12.],
##        [ 0.,  0.,  0.,  1.]])
