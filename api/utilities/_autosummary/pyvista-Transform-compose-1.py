# Define an arbitrary 4x4 affine transformation matrix and compose it.
#
import pyvista as pv
array = [
    [0.707, -0.707, 0, 0],
    [0.707, 0.707, 0, 0],
    [0, 0, 1, 1.5],
    [0, 0, 0, 2],
]
transform = pv.Transform().compose(array)
transform.matrix
# Expected:
## array([[ 0.707, -0.707,  0.   ,  0.   ],
##        [ 0.707,  0.707,  0.   ,  0.   ],
##        [ 0.   ,  0.   ,  1.   ,  1.5  ],
##        [ 0.   ,  0.   ,  0.   ,  2.   ]])
#
# Define a second transformation and use ``+`` to compose it.
#
array = [[1, 0, 0], [0, 0, -1], [0, -1, 0]]
transform = transform * array
transform.matrix
# Expected:
## array([[ 0.707, -0.707,  0.   ,  0.   ],
##        [ 0.   ,  0.   , -1.   , -1.5  ],
##        [-0.707, -0.707,  0.   ,  0.   ],
##        [ 0.   ,  0.   ,  0.   ,  2.   ]])
