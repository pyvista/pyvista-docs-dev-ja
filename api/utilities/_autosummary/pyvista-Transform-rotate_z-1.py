# Compose a rotation about the z-axis.
#
import pyvista as pv
transform = pv.Transform().rotate_z(90)
transform.matrix
# Expected:
## array([[ 0., -1.,  0.,  0.],
##        [ 1.,  0.,  0.,  0.],
##        [ 0.,  0.,  1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second rotation about the z-axis.
#
_ = transform.rotate_z(45)
#
# The result is a matrix that rotates about the z-axis by 135 degrees.
#
transform.matrix
# Expected:
## array([[-0.70710678, -0.70710678,  0.        ,  0.        ],
##        [ 0.70710678, -0.70710678,  0.        ,  0.        ],
##        [ 0.        ,  0.        ,  1.        ,  0.        ],
##        [ 0.        ,  0.        ,  0.        ,  1.        ]])
