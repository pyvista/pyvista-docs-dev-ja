# Create a transform by concatenating scaling, rotation, and translation
# matrices.
#
import numpy as np
import pyvista as pv
transform = pv.Transform()
_ = transform.scale(1, 2, 3)
_ = transform.rotate_z(90)
_ = transform.translate(4, 5, 6)
transform
# Expected:
## Transform (...)
##   Num Transformations: 3
##   Matrix:  [[ 0., -2.,  0.,  4.],
##             [ 1.,  0.,  0.,  5.],
##             [ 0.,  0.,  3.,  6.],
##             [ 0.,  0.,  0.,  1.]]
#
# Decompose the matrix.
#
T, R, N, S, K = transform.decompose()
#
# Since the input has no shear this component is the identity matrix.
# Similarly, there are no reflections so its value is ``1``. All other components
# are recovered perfectly and match the input.
#
K  # shear
# Expected:
## array([[1., 0., 0.],
##        [0., 1., 0.],
##        [0., 0., 1.]])
#
S  # scale
# Expected:
## array([1., 2., 3.])
#
N  # reflection
# Expected:
## array(1.)
#
R  # rotation
# Expected:
## array([[ 0., -1.,  0.],
##        [ 1.,  0.,  0.],
##        [ 0.,  0.,  1.]])
#
T  # translation
# Expected:
## array([4., 5., 6.])
#
# Compose a shear component using pre-multiplication so that shearing is
# the first transformation.
#
shear = np.eye(4)
shear[0, 1] = 0.1  # xy shear
_ = transform.compose(shear, multiply_mode='pre')
#
# Repeat the decomposition and show its components. Note how the decomposed shear
# does not perfectly match the input shear matrix values. The values of the
# scaling and rotation components are also affected and do not exactly match the
# input. This is expected, because the shear can be partially factored as a
# combination of rotation and scaling.
#
T, R, N, S, K = transform.decompose()
#
K  # shear
# Expected:
## array([[1.        , 0.03333333, 0.        ],
##        [0.01663894, 1.        , 0.        ],
##        [0.        , 0.        , 1.        ]])
#
S  # scale
# Expected:
## array([0.99944491, 2.0022213 , 3.        ])
#
N  # reflection
# Expected:
## array(1.)
#
R  # rotation
# Expected:
## array([[ 0.03331483, -0.99944491,  0.        ],
##        [ 0.99944491,  0.03331483,  0.        ],
##        [ 0.        ,  0.        ,  1.        ]])
#
T  # translation
# Expected:
## array([4., 5., 6.])
#
# Although the values may not match the input exactly, the decomposition is
# nevertheless valid and can be used to re-compose the original transformation.
#
T, R, N, S, K = transform.decompose(homogeneous=True)
T @ R @ N @ S @ K
# Expected:
## array([[-5.76153045e-17, -2.00000000e+00,  0.00000000e+00,
##          4.00000000e+00],
##        [ 1.00000000e+00,  1.00000000e-01,  0.00000000e+00,
##          5.00000000e+00],
##        [ 0.00000000e+00,  0.00000000e+00,  3.00000000e+00,
##          6.00000000e+00],
##        [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
##          1.00000000e+00]])
#
# Alternatively, re-compose the transformation as a new
# :class:`~pyvista.Transform` with pre-multiplication.
#
recomposed = pv.Transform([T, R, N, S, K], multiply_mode='pre')
np.allclose(recomposed.matrix, transform.matrix)
# Expected:
## True
#
# Compose a reflection and decompose the transform again.
#
_ = transform.flip_x()
T, R, N, S, K = transform.decompose()
#
# The reflection component is now ``-1``.
#
N  # reflection
# Expected:
## array(-1.)
#
# The decomposition may be simplified to a ``TRSK`` decomposition by combining
# the reflection component with either the rotation or the scaling term.
#
# Multiplying the reflection with the rotation will make it a left-handed rotation
# with negative determinant:
#
R = R * N
np.linalg.det(R) < 0
# Expected:
## np.True_
#
# Alternatively, keep the rotation right-handed but make the scaling factors negative:
#
S = S * N
S  # scale
# Expected:
## array([-0.99944491, -2.0022213 , -3.        ])
