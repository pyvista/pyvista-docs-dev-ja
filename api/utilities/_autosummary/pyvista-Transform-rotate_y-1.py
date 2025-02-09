# Compose a rotation about the y-axis.
#
import pyvista as pv
transform = pv.Transform().rotate_y(90)
transform.matrix
# Expected:
## array([[ 0.,  0.,  1.,  0.],
##        [ 0.,  1.,  0.,  0.],
##        [-1.,  0.,  0.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second rotation about the y-axis.
#
_ = transform.rotate_y(45)
#
# The result is a matrix that rotates about the y-axis by 135 degrees.
#
transform.matrix
# Expected:
## array([[-0.70710678,  0.        ,  0.70710678,  0.        ],
##        [ 0.        ,  1.        ,  0.        ,  0.        ],
##        [-0.70710678,  0.        , -0.70710678,  0.        ],
##        [ 0.        ,  0.        ,  0.        ,  1.        ]])
