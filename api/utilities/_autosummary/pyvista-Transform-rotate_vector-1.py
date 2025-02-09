# Compose a rotation of 30 degrees about the ``(1, 1, 1)`` axis.
#
import pyvista as pv
transform = pv.Transform().rotate_vector((1, 1, 1), 30)
transform.matrix
# Expected:
## array([[ 0.9106836 , -0.24401694,  0.33333333,  0.        ],
##        [ 0.33333333,  0.9106836 , -0.24401694,  0.        ],
##        [-0.24401694,  0.33333333,  0.9106836 ,  0.        ],
##        [ 0.        ,  0.        ,  0.        ,  1.        ]])
#
# Compose a second rotation of 45 degrees about the ``(1, 2, 3)`` axis.
#
_ = transform.rotate_vector((1, 2, 3), 45)
transform.matrix
# Expected:
## array([[ 0.38042304, -0.50894634,  0.77217351,  0.        ],
##        [ 0.83349512,  0.55045308, -0.04782562,  0.        ],
##        [-0.40070461,  0.66179682,  0.63360933,  0.        ],
##        [ 0.        ,  0.        ,  0.        ,  1.        ]])
