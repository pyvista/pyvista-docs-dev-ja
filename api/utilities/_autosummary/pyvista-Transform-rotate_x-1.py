# Compose a rotation about the x-axis.
#
import pyvista as pv
transform = pv.Transform().rotate_x(90)
transform.matrix
# Expected:
## array([[ 1.,  0.,  0.,  0.],
##        [ 0.,  0., -1.,  0.],
##        [ 0.,  1.,  0.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second rotation about the x-axis.
#
_ = transform.rotate_x(45)
#
# The result is a matrix that rotates about the x-axis by 135 degrees.
#
transform.matrix
# Expected:
## array([[ 1.        ,  0.        ,  0.        ,  0.        ],
##        [ 0.        , -0.70710678, -0.70710678,  0.        ],
##        [ 0.        ,  0.70710678, -0.70710678,  0.        ],
##        [ 0.        ,  0.        ,  0.        ,  1.        ]])
