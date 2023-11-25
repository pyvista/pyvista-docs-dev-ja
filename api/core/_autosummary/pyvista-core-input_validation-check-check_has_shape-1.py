# Check if an array is one-dimensional.
#
import numpy as np
import pyvista.core.input_validation as valid
valid.check_has_shape([1, 2, 3], shape=(-1))
#
# Check if an array is one-dimensional or a scalar.
#
valid.check_has_shape(1, shape=[(), (-1)])
#
# Check if an array is 3x3 or 4x4.
#
valid.check_has_shape(np.eye(3), shape=[(3, 3), (4, 4)])
